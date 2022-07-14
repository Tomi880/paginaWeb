from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from crud.models import *
from .serializers import *
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST','DELETE'])
def lista_productos(request):
    #Obtener uno o muchos
    if request.method == 'GET':
        productos = Producto.objects.all()

        productos_serializer = ProductoSerializer(productos,many=True)
        
        return Response(productos_serializer.data)

    #Crear un nuevo producto
    elif request.method == 'POST':
        producto_data = JSONParser().parse(request)
        productos_serializer = ProductoSerializer(data=producto_data)
        if productos_serializer.is_valid():
            productos_serializer.save()
            return Response(productos_serializer.data,status=status.HTTP_201_CREATED)
        return Response(productos_serializer.error,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Producto.objects.all().delete()
        return Response({'mensaje':'{} productos han sido eliminados desde la base de datos!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def detalle_productos(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
    except:
        return Response({'mensaje':'El producto buscado no existe'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        producto_serializer = ProductoSerializer(producto)
        return Response(producto_serializer.data)

    elif request.method == 'PUT':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(producto,data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(producto_serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        producto.delete()
        return Response({'mensaje':'El producto {} ha sido eliminado desde la base de datos!'.format(product_id)},status=status.HTTP_204_NO_CONTENT)

    
@api_view(['GET','POST','DELETE'])
def lista_marca(request):
    #Obtener uno o muchos
    if request.method == 'GET':
        marcas = Marca.objects.all()

        marcas_serializer = MarcaSerializer(marcas,many=True)
        
        return Response(marcas_serializer.data)