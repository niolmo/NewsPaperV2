from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Sum


class Author(models.Model):
    author = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Автор')
    auRunk = models.IntegerField(default=0, verbose_name='Рейтинг')

    # МЕТОДЫ

    def update_rating(self):
        poRunk = self.post_set.all().aggregate(postRating=Sum('runk'))
        p_R = 0
        p_R += poRunk.get('postRating')

        comRunk = self.author.comment_set.all().aggregate(commRating=Sum('runk'))
        c_R = 0
        c_R += comRunk.get('commRating')

        self.authorRunk = p_R * 3 + c_R
        self.save()

    class Meta:
        managed = True
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.author}'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    class Meta:
        ordering = ['-name']
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    # варианты типов + кортеж
    news = 'NW'
    artical = 'AR'
    types = [
        (news, 'Новость'),
        (artical, 'Статья')
    ]
    publ = models.DateField(default=timezone.now, verbose_name='Дата')
    sort = models.CharField(max_length=2, choices=types, default=news)
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, verbose_name='Адрес')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name='Автор')
    runk = models.IntegerField(default=0, verbose_name='Рейтинг')

    # МЕТОДЫ
    def like(self):
        self.runk += 1
        self.save()

    def dislike(self):
        self.runk -= 1
        self.save()

    def preview(self):
        return self.text[0: 124] + '...'

    class Meta:
        ordering = ['-publ']
        managed = True
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        indexes = [models.Index(fields=['-publ'])]

    def __str__(self):
        return f'{self.publ}, {self.sort}, {self.categories}, {self.title}, {self.slug}, {self.text}, {self.author}, {self.runk},'


class Comments(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Пост')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    publ = models.DateField(default=timezone.now, verbose_name='Дата')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    runk = models.IntegerField(default=0, verbose_name='Рейтинг')

    # МЕТОДЫ

    def like(self):
        self.runk += 1
        self.save()

    def dislike(self):
        self.runk -= 1
        self.save()

    class Meta:
        ordering = ['-publ']
        managed = True
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментари'
        indexes = [models.Index(fields=['-publ'])]

    def __str__(self):
        return f'{self.post}, {self.user}, {self.publ}, {self.title}, {self.text}, {self.runk},'
