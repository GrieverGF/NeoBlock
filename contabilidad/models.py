from django.db import models
from django.contrib.auth.models import User

class CuentaContable(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=[('activo', 'Activo'), ('pasivo', 'Pasivo'), ('ingreso', 'Ingreso'), ('gasto', 'Gasto')])
    padre = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcuentas')

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class AsientoContable(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def total_debitos(self):
        return sum([l.debito for l in self.lineas.all()])

    def total_creditos(self):
        return sum([l.credito for l in self.lineas.all()])

    def esta_balanceado(self):
        return self.total_debitos() == self.total_creditos()

class LineaAsiento(models.Model):
    asiento = models.ForeignKey(AsientoContable, on_delete=models.CASCADE, related_name='lineas')
    cuenta = models.ForeignKey(CuentaContable, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=200)
    debito = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credito = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.cuenta.nombre}: D {self.debito} / C {self.credito}"