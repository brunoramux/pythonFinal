from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    end_log = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)