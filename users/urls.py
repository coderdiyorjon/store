from django.urls import path
from users.views import UserLoginView, register, profile
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),]