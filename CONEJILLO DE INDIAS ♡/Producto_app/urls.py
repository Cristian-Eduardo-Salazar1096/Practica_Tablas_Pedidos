from django.urls import path
from Producto_app import views
urlpatterns = [
    path('', views.inicio_vista, name="inicio_vista"),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<int:id>",views.seleccionarProducto,name="seleccionarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<int:id>",views.borrarProducto,name="borrarProducto"),
]