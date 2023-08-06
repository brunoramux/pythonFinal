from django.shortcuts import render
from django.views.generic import ListView, CreateView
from chamados.models import Chamados
from django.urls import reverse_lazy

# Create your views here.
class ChamadoList(ListView):
    model = Chamados
    queryset = Chamados.objects.all()
    
    
class ChamadoCreate(CreateView):
    model = Chamados 
    fields = '__all__'
    success_url = reverse_lazy('create')