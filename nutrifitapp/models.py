from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse_lazy


# Create your models here.

#class Categoria(models.Model):
#    nombre = models.CharField(max_length=255)
#
#    def __str__(self):
#        return self.nombre

#    def get_absolute_url(self):
#        return reverse_lazy("inicio")


class Producto(models.Model):
    titulo = models.CharField(max_length=255)
    precio = models.CharField(max_length=100)
    cantidad_disponible = models.CharField(max_length=255)
    arte_imagen = models.ImageField(null=True, blank=True,  upload_to="imagenes/")
    #categoria = models.CharField(max_length=255, default="sin categoría")

    def __str__(self):
        return self.titulo

