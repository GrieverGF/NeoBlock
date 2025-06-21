from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.db import transaction
from .models import Factura
from .forms import FacturaForm, LineaFacturaFormSet

class FacturaListView(ListView):
    model = Factura
    template_name = "facturacion/factura_list.html"
    context_object_name = "facturas"

class FacturaCreateView(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = "facturacion/factura_form.html"
    success_url = reverse_lazy('facturacion:factura_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['lineas_formset'] = LineaFacturaFormSet(self.request.POST)
        else:
            context['lineas_formset'] = LineaFacturaFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        lineas_formset = context['lineas_formset']
        if lineas_formset.is_valid():
            with transaction.atomic():
                factura = form.save()
                lineas_formset.instance = factura
                lineas_formset.save()
                factura.total = sum(lf.subtotal for lf in factura.lineas.all())
                factura.save()
            return redirect(self.success_url)
        return self.render_to_response(self.get_context_data(form=form))