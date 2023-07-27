from django.shortcuts import render
from django.views.generic.base import View
from .models import Post


class PostView(View):
    def get(serf, request):
        posts = Post.objects.all()
        return render(request, 'news.html', {'post_list': posts})
