from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Empresa

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Campo Obrigatório')
    last_name = forms.CharField(max_length=30, required=True, help_text='Campo Obrigatório')
    email = forms.EmailField(required=False, help_text='Obrigatório. Por favor insira um e-mail válido')

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2'}



    