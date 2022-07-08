from django.urls import path
from .views import *

urlpatterns = [
    path('', lista_productos,name="lista-productos"),
    path('new',nuevo_producto,name="nuevo-producto"),
    path('<str:product_id>',form_productos,name="form-productos"),
]