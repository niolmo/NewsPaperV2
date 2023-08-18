from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from .models import Post
from django.core.paginator import Paginator


class PostView(View):
    def get(serf, request):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 3)
        page_nuber = request.GET.get('page', 1)
        posts = paginator.page(page_nuber)
        return render(request, 'news.html', {'post_list': posts})


class Search(ListView):
    pass