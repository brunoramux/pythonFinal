from django.shortcuts import render
from django.views.generic import ListView, CreateView
from clientes.models import Cliente
from django.urls import reverse_lazy

# Create your views here.
class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    
    
class ClienteCreate(CreateView):
    model = Cliente 
    fields = '__all__'
    success_url = reverse_lazy('index')