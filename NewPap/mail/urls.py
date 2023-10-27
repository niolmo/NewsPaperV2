from django.urls import path
from .views import MailView

app_name = 'mail'

urlpatterns = [
    path('make', MailView.as_view(), name='make')
]
