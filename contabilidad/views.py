from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CuentaContable

class CuentaContableListView(ListView):
    model = CuentaContable
    template_name = 'contabilidad/cuenta_list.html'
    context_object_name = 'cuentas'

class CuentaContableCreateView(CreateView):
    model = CuentaContable
    fields = ['codigo', 'nombre', 'tipo', 'padre']
    template_name = 'contabilidad/cuenta_form.html'
    success_url = reverse_lazy('contabilidad:lista_cuentas')

class CuentaContableUpdateView(UpdateView):
    model = CuentaContable
    fields = ['codigo', 'nombre', 'tipo', 'padre']
    template_name = 'contabilidad/cuenta_form.html'
    success_url = reverse_lazy('contabilidad:lista_cuentas')

class CuentaContableDeleteView(DeleteView):
    model = CuentaContable
    template_name = 'contabilidad/cuenta_confirm_delete.html'
    success_url = reverse_lazy('contabilidad:lista_cuentas')
