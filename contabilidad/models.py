from django.db import models
from django.contrib.auth.models import User  # Para campo creado_por (usuario)

class CuentaContable(models.Model):
    """Catálogo de cuentas contables."""
    TIPO_CUENTA = [
        ('ACTIVO', 'Activo'),
        ('PASIVO', 'Pasivo'),
        ('PATRIMONIO', 'Patrimonio'),
        ('INGRESO', 'Ingreso'),
        ('GASTO', 'Gasto'),
    ]
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CUENTA)
    padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)  # Cuenta padre opcional (jerarquía)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class AsientoContable(models.Model):
    """Encabezado de un asiento contable (transacción)."""
    fecha = models.DateField()
    descripcion = models.TextField()
    creado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Asiento {self.id} - {self.fecha} - {self.descripcion[:30]}"

    # (Opcional) Validación de balance en modelo – verificado también vía formulario
    def clean(self):
        total_debito = sum(line.debito for line in getattr(self, "lineas", []).all())
        total_credito = sum(line.credito for line in getattr(self, "lineas", []).all())
        if total_debito != total_credito:
            from django.core.exceptions import ValidationError
            raise ValidationError("El asiento no está balanceado: la suma de débitos y créditos difiere:contentReference[oaicite:0]{index=0}")

class LineaAsiento(models.Model):
    """Línea individual de un asiento contable (movimiento de débito o crédito)."""
    asiento = models.ForeignKey(AsientoContable, related_name='lineas', on_delete=models.CASCADE)
    cuenta = models.ForeignKey(CuentaContable, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=200, blank=True)
    debito = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credito = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.cuenta.codigo} - Débito: {self.debito} | Crédito: {self.credito}"
