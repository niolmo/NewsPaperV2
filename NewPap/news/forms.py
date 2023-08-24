from django.forms import ModelForm
from .models import *


class PosForm(ModelForm):
    class Meta:
        model = Post
        fields = ['publ', 'sort', 'categories',
                  'title', 'text', 'author']
