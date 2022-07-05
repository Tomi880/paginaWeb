from django.shortcuts import render
from .models import *
# Create your views here.

def product_list(request):
    context = {'productos':Producto.objects.all()}
    return render(request,'core/productos.html',context)