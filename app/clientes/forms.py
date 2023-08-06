from django import forms
from models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta: 
        model = Cliente
        field = '__all__'