from django.urls import include
from .views import *
from django.urls import path

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login')
    ]
