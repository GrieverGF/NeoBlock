from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="empleado_personal")
    identificacion = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.cargo}"
