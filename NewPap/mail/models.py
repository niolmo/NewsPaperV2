from django.db import models
from datetime import datetime


class MailModel(models.Model):
    email = models.EmailField()
    date = models.DateField(default=datetime.now)
    user_name = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name = ("Письмо")
        verbose_name_plural = ("Письма")

    def __str__(self):
        return f'{self.user_name}: {self.message}'
