from django import forms
from .models import PagoNomina
from empleado.models import Empleado

class PagoNominaForm(forms.ModelForm):
    class Meta:
        model = PagoNomina
        fields = ['empleado', 'periodo', 'valor', 'descripcion']

