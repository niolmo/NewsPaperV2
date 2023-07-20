from django.contrib import admin
from .models import *


@admin.register(Author)
class AuAam(admin.ModelAdmin):
    list_display = ['author', 'auRunk']
    raw_id_fields = ['author']


admin.site.register(Category)


@admin.register(Post)
class PostAdm(admin.ModelAdmin):
    list_display = ['publ', 'sort', 'title', 'slug', 'author', 'runk']
    list_filter = ['publ', 'title', 'author']
    filter_horizontal = ['categories']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']


@admin.register(Comments)
class ComADM(admin.ModelAdmin):
    list_display = ['publ', 'post', 'user', 'runk']
