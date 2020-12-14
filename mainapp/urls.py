from django.contrib import admin
from django.urls import path
from .views import index, signup, home

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('home/', home, name='home')
]
