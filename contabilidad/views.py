from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.db import transaction
from .models import AsientoContable
from .forms import AsientoForm, LineaAsientoFormSet

class AsientoListView(ListView):
    model = AsientoContable
    template_name = "contabilidad/asiento_list.html"
    context_object_name = "asientos"

class AsientoCreateView(CreateView):
    model = AsientoContable
    form_class = AsientoForm
    template_name = "contabilidad/asiento_form.html"
    success_url = reverse_lazy('contabilidad:asiento_listar')  # URL de redirección tras crear
    
    def get_context_data(self, **kwargs):
        """Inyecta el formset de líneas en el contexto para renderizar en la plantilla."""
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['lineas_formset'] = LineaAsientoFormSet(self.request.POST)
        else:
            context['lineas_formset'] = LineaAsientoFormSet()
        return context

    def form_valid(self, form):
        """Guarda el nuevo asiento y sus líneas si todas las formas son válidas."""
        context = self.get_context_data()
        lineas_formset = context['lineas_formset']
        if lineas_formset.is_valid():
            # Asignar el usuario que crea el asiento antes de guardar
            asiento = form.save(commit=False)
            asiento.creado_por = self.request.user
            # Usar una transacción atómica para guardar asiento y líneas juntos
            with transaction.atomic():
                asiento.save()
                # Asignar el asiento a cada línea y guardar las líneas
                lineas_formset.instance = asiento
                lineas_formset.save()
            return redirect(self.success_url)
        else:
            # Si el formset de líneas no es válido, re-renderizar el formulario con errores
            return self.render_to_response(self.get_context_data(form=form))
