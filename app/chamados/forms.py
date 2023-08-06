from django import forms
from models import Chamados
from django.forms.widgets import DateInput

class ChamadosForm(forms.ModelForm):
    createdAt = forms.DateField(label=u'Data de Criacao *',
    widget=DateInput(format='%d/%m/%Y', attrs={'maxlength':'10',
    'onkeyup':'formataData(this,event)'}), input_formats=['%d/%m/%Y',], )
    class Meta: 
        model = Chamados
        field = '__all__'