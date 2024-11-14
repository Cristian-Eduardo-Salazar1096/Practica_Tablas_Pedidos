from django.urls import path
from Pedidos_app import views
urlpatterns = [
    path('', views.inicio_vista, name="inicio_vista"),
    path("registrarPedido/",views.registrarPedido,name="registrarPedido"),
    path("seleccionarPedido/<int:id_pedido>",views.seleccionarPedido,name="seleccionarPedido"),
    path("editarPedido/",views.editarPedido,name="editarPedido"),
    path("borrarPedido/<int:id_pedido>",views.borrarPedido,name="borrarPedido"),
]