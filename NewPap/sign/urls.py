from django.urls import path
from .views import LoginFomView

app_name = 'Login'

urlpatterns = [
    path('login', LoginFomView.as_view(), name="Login"),
]
