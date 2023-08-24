from django.urls import path
from . import views
from .views import Search, NewsDetail, PostForm

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('search', Search.as_view(), name='search'),
    path('add', PostForm.as_view(), name='add'),
]
