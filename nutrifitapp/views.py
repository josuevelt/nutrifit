from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from django.urls import reverse_lazy
from .forms import ProductoForm

# Create your views here.

class AgregarProductoView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "agregar_tarea.html"
    #fields = "__all__"
    success_url = reverse_lazy("inicio")

class Inicio(ListView):
    model = Producto
    template_name = "inicio.html"

class ProductosView(ListView):
    model = Producto
    template_name = "producto.html"

class EditarProductoView(UpdateView):
    model = Producto
    template_name = "editar_producto.html"
    fields = "__all__"
    success_url = reverse_lazy("inicio")

class EliminarProductoView(DeleteView):
    model = Producto
    template_name = "eliminar_producto.html"
    success_url = reverse_lazy("inicio")


