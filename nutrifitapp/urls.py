from django.urls import path
from .views import AgregarProductoView, Inicio, EditarProductoView, EliminarProductoView

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    path("agregar_producto/", AgregarProductoView.as_view(), name="agregar_producto"),
    path("editar_producto/<int:pk>/", EditarProductoView.as_view(), name="editar_producto"),
    path("producto/<int:pk>/eliminar/", EliminarProductoView.as_view(), name="eliminar_producto"),

]
