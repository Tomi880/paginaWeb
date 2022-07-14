from django.urls import path
from .views import *

urlpatterns = [
    path('', lista_productos,name='lista_productos'),
    path('new/',nuevo_producto,name='nuevo_producto'),
    path('<str:product_id>/',detalle_productos,name="detalle_productos"),
    path('<str:product_id>/update',actualizar_productos,name='actualizar_productos'),
    path('<str:product_id>/delete',eliminar_productos,name='eliminar_productos'),
]