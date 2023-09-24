from django.urls import path
from . import views
from .views import Search, NewsDetail, PosForm, PostDelete, PostUp
from django.views.decorators.cache import cache_page

app_name = 'newsPort'

urlpatterns = [
    # Раз в 10 минут товар будет записываться в кэш для экономии ресурсов
    path('', cache_page(1*10)(views.PostView.as_view()), name='allnews'),
    path('<int:pk>', cache_page(5*10)(NewsDetail.as_view()), name='detail'),
    path('search', Search.as_view(), name='search'),
    path('add', PosForm.as_view(), name='add'),
    path('update/<int:pk>/', PostUp.as_view(), name='up'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
]
