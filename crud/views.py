from email.mime import image
from logging.config import stopListening
from math import prod
import re
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

from .forms import ProductoForm
from .models import *
# Create your views here.

def product_list(request):
    context = {'productos':Producto.objects.all()}
    return render(request,'crud/lista_productos.html',context)

def product_new(request):
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
            return redirect(reverse('lista_producto') + "?OK")
        else:
            return redirect(reverse('lista_producto') + "?FAIL")
    else:
        form = ProductoForm
    return render(request,'crud/nuevo_producto.html',{'form':form})