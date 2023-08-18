from django.urls import path
from . import views
from .views import Search

urlpatterns = [
    path('', views.PostView.as_view()),
    path('search', Search.as_view(), name='search'),
]
