from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import RegForm


class LoginFomView(LoginView):
    template_name = 'userlogin.html'
    form_class = AuthenticationForm


class NewsView(LoginRequiredMixin, TemplateView):
    template_name = 'news.html'


class RegView(CreateView):
    model = User
    form_class = RegForm
    template_name = 'reg.html'
    success_url = '/'
