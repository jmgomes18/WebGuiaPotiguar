from django.contrib import admin
from django.urls import path
from .views import index, signup, EmpresaCreate, EmpresaUpdateView, EmpresaDeleteView, EmpresaListView, EmpresaDetailView

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('empresas/', EmpresaListView.as_view(), name='empresa_list'),
    path("empresas/<int:pk>", EmpresaUpdateView.as_view(), name="empresa_update"),
    path("empresas/<int:pk>/delete", EmpresaDeleteView.as_view(), name="empresa_delete"),
    path("empresas/detail/<int:pk>", EmpresaDetailView.as_view(), name="empresa_detail"),
    path("empresas/registro_empresa/", EmpresaCreate.as_view(), name="empresa_form"),
]
