from email.mime import image
from logging.config import stopListening
from math import prod
import re
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

from .forms import ProductoForm
from .models import *
# Create your views here.

def lista_productos(request):
    context = {'productos':Producto.objects.all()}
    return render(request,'crud/lista_productos.html',context)

def detalle_productos(request, product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        if producto:
            context = {'producto':producto}
            return render(request,'crud/detalle_productos')
    except:
        return redirect(reverse('lista_productos') + "?FAIL")

def actualizar_productos(request, product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        form = ProductoForm(instance=producto)

        if request.method == 'POST':
            form = ProductoForm(request.POST,request.FILES,instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('lista_productos') + '?UPDATED')
            else:
                return redirect(reverse('actualizar_producto') + product_id)

        context = {'form':form}
        return render(request,'crud/actualizar_producto.html',context)
    except:
        return redirect(reverse('lista_productos') + "?NO_EXITS")

def eliminar_productos(request, product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        producto.delete()
        return redirect(reverse('lista_productos') + "?OK")
    except:
        return redirect(reverse('lista_productos') + "?FAIL")

def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            idProducto = form.cleaned_data.get("idProducto")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            stock = form.cleaned_data.get("stock")
            imagen = form.cleaned_data.get("imagen")
            marca = form.cleaned_data.get("marca")
            obj = Producto.objects.create(
                idProducto = idProducto,
                descripcion = descripcion,
                precio = precio,
                stock = stock,
                imagen = imagen,
                marca = marca
            )
            obj.save()
            return redirect(reverse('lista_productos') + "?OK")
        else:
            return redirect(reverse('lista_productos') + "?FAIL")
    else:
        form = ProductoForm
    return render(request,'crud/nuevo_producto.html',{'form':form})