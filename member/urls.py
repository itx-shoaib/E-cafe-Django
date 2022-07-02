from django.urls import path
from . import views


urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('login', views.handleLogin, name='login'),
    path('logout', views.handleLogout, name='logout'),
]