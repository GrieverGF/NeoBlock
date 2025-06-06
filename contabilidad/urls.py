from django.urls import path
from . import views

app_name = 'contabilidad'

urlpatterns = [
    path('cuentas/', views.CuentaContableListView.as_view(), name='lista_cuentas'),
    path('cuentas/nueva/', views.CuentaContableCreateView.as_view(), name='crear_cuenta'),
    path('cuentas/<int:pk>/editar/', views.CuentaContableUpdateView.as_view(), name='editar_cuenta'),
    path('cuentas/<int:pk>/eliminar/', views.CuentaContableDeleteView.as_view(), name='eliminar_cuenta'),
]
