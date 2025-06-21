from django.urls import path
from .views import AsientoListView, AsientoCreateView

app_name = 'contabilidad'
urlpatterns = [
    path('asientos/', AsientoListView.as_view(), name='asiento_listar'),
    path('asientos/nuevo/', AsientoCreateView.as_view(), name='asiento_crear'),
]
