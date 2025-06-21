# nomina/models.py
from django.db import models

class PagoNomina(models.Model):
    from empleado.models import Empleado  # importación retrasada para evitar ciclos
    empleado = models.ForeignKey('empleado.Empleado', on_delete=models.CASCADE)
    periodo = models.CharField(max_length=20)  # Ejemplo: "Junio 2025"
    fecha_pago = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Pago {self.periodo} - {self.empleado.user.get_full_name()}"

# nomina/forms.py
from django import forms
from .models import PagoNomina
from empleado.models import Empleado

class PagoNominaForm(forms.ModelForm):
    class Meta:
        model = PagoNomina
        fields = ['empleado', 'periodo', 'valor', 'descripcion']