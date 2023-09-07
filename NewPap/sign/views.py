from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import RegForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


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

    def form_valid(self, form):
        user = form.save()
        group = Group.objects.get_or_create(name='my_group')[0]
        user.groups.add('common')  # добавляем нового пользователя в эту группу
        user.save()
        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, TemplateView):
    template_name = 'account/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(
            name='author').exists()
        return context


@login_required
def upgrade_me(request):
    user = request.user
    autor_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        autor_group.user_set.add(user)
    return redirect('/')
