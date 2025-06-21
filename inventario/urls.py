from django.urls import path
from .views import ProductoListView, ProductoCreateView, MovimientoCreateView

app_name = 'inventario'

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='producto_listar'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto_crear'),
    path('movimientos/nuevo/', MovimientoCreateView.as_view(), name='movimiento_crear'),
]
