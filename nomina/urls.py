# nomina/urls.py
from django.urls import path
from . import views

app_name = 'nomina'

urlpatterns = [
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_listar'),
    path('nomina/nuevo/', views.PagoNominaCreateView.as_view(), name='pago_crear'),
]
