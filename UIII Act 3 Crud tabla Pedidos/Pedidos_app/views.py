from django.shortcuts import render,redirect
from .models import Pedidos
# Create your views here.

def inicio_vista(request):
    losPedidos=Pedidos.objects.all()
    return render(request,"gestionarPedidos.html",{"misPedidos":losPedidos})

def registrarPedido(request):
    id_pedido=request.POST["id_pedido"]
    nombre=request.POST["nombre"]
    fech=request.POST["fech"]
    id_Cliente=request.POST["id_Cliente"]
    Costo=request.POST["Costo"]
    Direccion=request.POST["Direccion"]
    Cantidad=request.POST["Cantidad"]
    guardarpedido=Pedidos.objects.create(id_pedido=id_pedido,nombre=nombre,fech=fech,id_Cliente=id_Cliente,Costo=Costo,Direccion=Direccion,Cantidad=Cantidad)
    return redirect("/")

def seleccionarPedido(request,id_pedido):
    pedido=Pedidos.objects.get(id_pedido=id_pedido)
    return render(request,"editarPedidos.html",{"misPedidos":pedido})

def editarPedido(request):
    id_pedido=request.POST["id_pedido"]
    nombre=request.POST["nombre"]
    fech=request.POST["fech"]
    id_Cliente=request.POST["id_Cliente"]
    Costo=request.POST["Costo"]
    Direccion=request.POST["Direccion"]
    Cantidad=request.POST["Cantidad"]
    pedido=Pedidos.objects.get(id_pedido=id_pedido)
    pedido.nombre=nombre
    pedido.fech=fech
    pedido.id_Cliente=id_Cliente
    pedido.Costo=Costo
    pedido.Direccion=Direccion
    pedido.Cantidad=Cantidad
    pedido.save()
    return redirect("/")


def borrarPedido(request, id_pedido):
    pedido = Pedidos.objects.get(id_pedido=id_pedido)
    pedido.delete()
    return redirect("/")