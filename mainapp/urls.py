from django.contrib import admin
from django.urls import path
from .views import index, signup, home, EmpresaCreate

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('home/', home, name='home'),
    path("home/registro_empresa/", EmpresaCreate.as_view(), name="registro_empresa")
]
