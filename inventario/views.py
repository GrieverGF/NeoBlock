from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Producto, MovimientoInventario
from .forms import ProductoForm, MovimientoInventarioForm

class ProductoListView(ListView):
    model = Producto
    template_name = "inventario/producto_list.html"
    context_object_name = "productos"

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "inventario/movimiento_form.html"
    success_url = reverse_lazy('inventario:producto_listar')

class MovimientoCreateView(CreateView):
    model = MovimientoInventario
    form_class = MovimientoInventarioForm
    template_name = "inventario/movimiento_form.html"
    success_url = reverse_lazy('inventario:producto_listar')