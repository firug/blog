from django.urls import path
from .views import SomeShittyClass

app_name = 'users'

urlpatterns = [
    path('users', SomeShittyClass.as_view(), name='users'),
]
