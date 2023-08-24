from django.forms import ModelForm
from django import forms
from .models import *


class PosForm(ModelForm):
    class Meta:
        model = Post
        fields = ['publ', 'sort', 'categories',
                  'title', 'text', 'author']
        widgets = {
            'publ': forms.DateInput(attrs={
                'class': 'fom-control',
            }),
            'sort': forms.Select(attrs={
                'class': 'fom-control',
            }),
            'categories': forms.Select(attrs={
                'class': 'fom-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'fom-control',
                'placeholder': 'Введите заголовог'
            }),
            'text': forms.Textarea(attrs={
                'class': 'fom-control',
                'placeholder': 'Текст новости'
            })
        }
