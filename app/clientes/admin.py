from django.contrib.admin import site
# Register your models here.
from clientes.models import Cliente 

site.register(Cliente)
