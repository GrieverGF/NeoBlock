from django.db import models

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.SET_NULL, null=True)
    stock = models.IntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    punto_reorden = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class MovimientoInventario(models.Model):
    ENTRADA = 'E'
    SALIDA = 'S'
    TIPO_CHOICES = [(ENTRADA, 'Entrada'), (SALIDA, 'Salida')]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.tipo == self.ENTRADA:
            self.producto.stock += self.cantidad
        elif self.tipo == self.SALIDA:
            self.producto.stock -= self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)
