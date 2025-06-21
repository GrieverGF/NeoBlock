from django.shortcuts import render
from contabilidad.models import LineaAsiento, CuentaContable
from django.db.models import Sum
from django.views import View

class BalanceGeneralView(View):
    def get(self, request):
        cuentas = CuentaContable.objects.all()
        saldos = []
        for cuenta in cuentas:
            total_debito = LineaAsiento.objects.filter(cuenta=cuenta).aggregate(Sum('debito'))['debito__sum'] or 0
            total_credito = LineaAsiento.objects.filter(cuenta=cuenta).aggregate(Sum('credito'))['credito__sum'] or 0
            saldo = total_debito - total_credito
            saldos.append({
                'cuenta': cuenta,
                'debito': total_debito,
                'credito': total_credito,
                'saldo': saldo,
            })
        return render(request, 'reportes/balance_general.html', {'saldos': saldos})