from django.shortcuts import render
from django.views.generic.base import View
from .models import Post
from django.core.paginator import Paginator


class PostView(View):
    def get(serf, request):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 3)
        page_nuber = request.GET.get('page', 1)
        posts = paginator.page(page_nuber)
        return render(request, 'news.html', {'post_list': posts})


class Search(View):
    def get(serf, request):
        search_list = Post.objects.filter(publ=request.GET.get('q')).filter(
            title=request.GET.get('d')).filter(author__username=request.GET.get('a'))
        paginator = Paginator(search_list, 3)
        page_nuber = request.GET.get('page', 1)
        posts = paginator.page(page_nuber)
        return render(request, 'search.html', {'search_list': posts})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get('q')
        context["d"] = self.request.GET.get('d')
        context["a"] = self.request.GET.get('a')
        return context
