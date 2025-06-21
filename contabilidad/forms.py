from django import forms
from django.forms import BaseInlineFormSet, inlineformset_factory
from .models import AsientoContable, LineaAsiento

class AsientoForm(forms.ModelForm):
    class Meta:
        model = AsientoContable
        fields = ['fecha', 'descripcion']  # creado_por y creado_en se asignan automáticamente

# Definimos una clase base para agregar validación al formset de líneas
class BaseLineaAsientoFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        total_debito = 0
        total_credito = 0
        # Sumamos débitos y créditos de todas las líneas válidas en el formset
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                total_debito += form.cleaned_data.get('debito', 0) or 0
                total_credito += form.cleaned_data.get('credito', 0) or 0
        # Verificar la regla de partida doble: debitos == creditos
        if total_debito != total_credito:
            raise forms.ValidationError("Los débitos y créditos del asiento no están balanceados:contentReference[oaicite:3]{index=3}")

# Crear el formset de líneas de asiento asociado a AsientoContable
LineaAsientoFormSet = inlineformset_factory(
    AsientoContable, LineaAsiento,
    formset=BaseLineaAsientoFormSet,
    fields=['cuenta', 'descripcion', 'debito', 'credito'],
    extra=2, can_delete=True
)
