from django.shortcuts import render,redirect
from .models import Provedores
# Create your views here.

def inicio_vista(request):
    losProvedores=Provedores.objects.all()
    return render(request,"gestionarProvedores.html",{"misProvedores":losProvedores})

def registrarProvedor(request):
    id_provedor=request.POST["id_provedor"]
    nombre=request.POST["nombre"]
    Telefono=request.POST["Telefono"]
    sucursal=request.POST["sucursal"]
    direccion=request.POST["direccion"]
    horario=request.POST["horario"]
    id_producto=request.POST["id_producto"]
    guardarprovedor=Provedores.objects.create(id_provedor=id_provedor,nombre=nombre,Telefono=Telefono,sucursal=sucursal,direccion=direccion,horario=horario,id_producto=id_producto)
    return redirect("/")

def seleccionarProvedor(request,id_provedor):
    provedor=Provedores.objects.get(id_provedor=id_provedor)
    return render(request,"editarProvedores.html",{"misProvedores":provedor})

def editarProvedor(request):
    id_provedor=request.POST["id_provedor"]
    nombre=request.POST["nombre"]
    Telefono=request.POST["Telefono"]
    sucursal=request.POST["sucursal"]
    direccion=request.POST["direccion"]
    horario=request.POST["horario"]
    id_producto=request.POST["id_producto"]
    provedor=Provedores.objects.get(id_provedor=id_provedor)
    provedor.nombre=nombre
    provedor.Telefono=Telefono
    provedor.sucursal=sucursal
    provedor.direccion=direccion
    provedor.horario=horario
    provedor.id_producto=id_producto
    provedor.save()
    return redirect("/")

def borrarProvedor(request, id_provedor):
    provedor = Provedores.objects.get(id_provedor=id_provedor)
    provedor.delete()
    return redirect("/")