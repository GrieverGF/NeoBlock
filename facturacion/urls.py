from django.urls import path
from .views import FacturaListView, FacturaCreateView

app_name = 'facturacion'

urlpatterns = [
    path('facturas/', FacturaListView.as_view(), name='factura_listar'),
    path('facturas/nueva/', FacturaCreateView.as_view(), name='factura_crear'),
]
