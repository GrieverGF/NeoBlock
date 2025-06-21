from django.urls import path
from .views import BalanceGeneralView

app_name = 'reportes'

urlpatterns = [
    path('balance/', BalanceGeneralView.as_view(), name='balance_general'),
]