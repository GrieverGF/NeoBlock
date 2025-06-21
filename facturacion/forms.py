from django import forms
from django.forms import inlineformset_factory
from .models import Factura, LineaFactura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente']

LineaFacturaFormSet = inlineformset_factory(
    Factura, LineaFactura,
    fields=['producto', 'cantidad', 'precio_unitario'],
    extra=1, can_delete=True
)