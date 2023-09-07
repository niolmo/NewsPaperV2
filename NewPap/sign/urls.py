from django.urls import path
from .views import LoginFomView, RegView, LogoutView, ProfileView
from .views import upgrade_me

app_name = 'login'

urlpatterns = [
    path('login', LoginFomView.as_view(), name="Login"),
    path('signup/', RegView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('upgrade/', upgrade_me, name='upgrade'),
]
