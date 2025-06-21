from django.contrib import admin
from .models import CuentaContable, AsientoContable, LineaAsiento

@admin.register(CuentaContable)
class CuentaContableAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'tipo', 'padre')
    search_fields = ('codigo', 'nombre', 'tipo')

class LineaAsientoInline(admin.TabularInline):
    model = LineaAsiento
    extra = 1  # líneas extra editables en admin

@admin.register(AsientoContable)
class AsientoContableAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'descripcion', 'creado_por', 'creado_en')
    date_hierarchy = 'fecha'
    inlines = [LineaAsientoInline]  # permitir gestionar líneas dentro del asiento
