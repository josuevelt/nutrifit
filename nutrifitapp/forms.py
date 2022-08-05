from django import forms
from .models import Producto, Categoria

categorias = Categoria.objects.all().values_list("nombre", "nombre")
lista_de_categorias = []

for queryitem_categoria in categorias:
    lista_de_categorias.append(queryitem_categoria)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("titulo", "precio", "cantidad_disponible", "arte_imagen", "categoria")

        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "titulo"}),
            "precio": forms.TextInput(),
            "cantidad_dispobible": forms.TextInput(),
            "categoria": forms.Select(choices=lista_de_categorias)
        }