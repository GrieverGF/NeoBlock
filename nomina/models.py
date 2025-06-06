from django.db import models
from inventario.models import Producto
from django.contrib.auth.models import User


class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    salario_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.user.get_full_name()

class Nomina(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    salario_bruto = models.DecimalField(max_digits=10, decimal_places=2)
    deducciones = models.DecimalField(max_digits=10, decimal_places=2)
    salario_neto = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_neto(self):
        self.salario_neto = self.salario_bruto - self.deducciones