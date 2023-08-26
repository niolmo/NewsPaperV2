from django.urls import path
from . import views
from .views import Search, NewsDetail, PosForm, PostDelete, PostUp

app_name = 'newsPort'

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='detail'),
    path('search', Search.as_view(), name='search'),
    path('add', PosForm.as_view(), name='add'),
    path('update/<int:pk>/', PostUp.as_view(), name='up'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
]
