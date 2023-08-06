from django.db import models

from clientes.models import Cliente

# Create your models here.
class Chamados(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    createdAt = models.DateField(auto_now_add=True)
