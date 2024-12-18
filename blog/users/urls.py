from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('singup/', views.signup, name='signup'),
]
