from mainapp.forms import SignupForm
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Empresa
from django.urls import reverse, reverse_lazy

# Create your views here.

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ["razao_social","cnpj","email","endereco","cidade","estado",]
    success_url = reverse_lazy('home')
    template_name = 'mainapp/empresa_form.html'

def index(request):
    return render(request, 'index.html', {})

def home(request):
    return render(request, 'home.html',{})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

