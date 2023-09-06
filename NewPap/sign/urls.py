from django.urls import path
from .views import LoginFomView, RegView, LogoutView

app_name = 'Login'

urlpatterns = [
    path('login', LoginFomView.as_view(), name="Login"),
    path('signup/', RegView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
