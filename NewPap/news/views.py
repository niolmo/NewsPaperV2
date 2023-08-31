from datetime import datetime
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import Post
from .forms import PosForm
from django.core.paginator import Paginator
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import LoginForm


class PostView(View):
    def get(serf, request):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 3)
        page_nuber = request.GET.get('page', 1)
        posts = paginator.page(page_nuber)
        return render(request, 'news.html', {'post_list': posts})


class Search(ListView):
    model = Post
    template_name = 'search.html'
    paginate_by = 3
    ordering = ['publ']

    def get_context_data(self, *, object_list=Post.objects.filter(), **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = PostFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'item.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now
        context['value'] = None
        return context


# class PostForm(ListView):
#     model = Post
#     template_name = 'addpost.html'
#     context_object_name = 'post'
#     ordering = ['publ']

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['choices'] = Post.types
#         context['form'] = PosForm()
#         return context

#     def formCreate(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return super().get(request, *args, **kwargs)
class PosForm(CreateView):
    template_name = 'addpost.html'
    form_class = PosForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def formCreate(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return super().get(request, *args, **kwargs)


class PostUp(UpdateView):
    template_name = 'addpost.html'
    fields = ['publ', 'sort', 'categories',
              'title', 'text', 'author']
    template_name_suffix = '_update_form'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('newsPort:allnews')


class LoginFormView(TemplateView):
    template_name = 'userlogin.html'
    frorm_class = LoginForm
