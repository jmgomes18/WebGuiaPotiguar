from mainapp.forms import SignupForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Empresa
from django.utils import timezone
from django.urls import reverse, reverse_lazy

# Create your views here.



class EmpresaCreate(CreateView):
    model = Empresa
    fields = ["razao_social","cnpj","email","endereco","cidade","estado",]
    success_url = reverse_lazy('empresa_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = ["razao_social","cnpj","email","endereco","cidade","estado",]
    success_url = reverse_lazy('empresa_list')

class EmpresaDeleteView(DeleteView):
    model = Empresa
    success_url = reverse_lazy('empresa_list')

class EmpresaListView(ListView):
    model = Empresa

    def get_queryset(self):
        return Empresa.objects.filter(user=self.request.user)
    
class EmpresaDetailView(DetailView):
    model = Empresa
    

def index(request):
    return render(request, 'index.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


