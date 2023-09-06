from django.urls import path
from .views import LoginFomView, RegView

app_name = 'Login'

urlpatterns = [
    path('login', LoginFomView.as_view(), name="Login"),
    path('signup/', RegView.as_view(), name='signup'),

]
