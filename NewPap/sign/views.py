from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class LoginFomView(LoginView):
    template_name = 'userlogin.html'
    form_class = AuthenticationForm
