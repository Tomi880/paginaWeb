from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def root(request):
    return redirect('/index')

def index(request):
    return render(request,"core/index.html")

def nosotros(request):
    return render(request,"core/nosotros.html")

def contacto(request):
    return render(request,"core/contacto.html")

def apiSismos(request):
    return render(request,"core/apiSismos.html")

def productos(request):
    return render(request,"core/productos.html")