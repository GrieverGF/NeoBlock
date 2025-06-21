from django import forms
from .models import Producto, MovimientoInventario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'categoria', 'stock', 'precio_unitario', 'punto_reorden']

class MovimientoInventarioForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        fields = ['producto', 'cantidad', 'tipo', 'descripcion']