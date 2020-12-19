from django.contrib import admin
from django.urls import path
from .views import index, signup, EmpresaCreate, EmpresaUpdateView, EmpresaDeleteView, listar_empresa

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('home/', listar_empresa, name='home'),
    path("home/registro_empresa/", EmpresaCreate.as_view(), name="registro_empresa"),
    path("home/registro_empresa/<int:pk>", EmpresaUpdateView.as_view(), name="update_empresa"),
    path("home/registro_empresa/<int:pk>/delete", EmpresaDeleteView.as_view(), name="delete_empresa"),
]
