from django.contrib.admin import site
# Register your models here.
from chamados.models import Chamados 

site.register(Chamados)