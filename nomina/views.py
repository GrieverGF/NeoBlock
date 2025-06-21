# nomina/views.py
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PagoNomina
from .forms import PagoNominaForm
from empleado.models import Empleado

class EmpleadoListView(ListView):
    model = Empleado
    template_name = "nomina/empleado_list.html"
    context_object_name = "empleados"

class PagoNominaCreateView(CreateView):
    model = PagoNomina
    form_class = PagoNominaForm
    template_name = "nomina/pago_form.html"
    success_url = reverse_lazy('nomina:empleado_listar')