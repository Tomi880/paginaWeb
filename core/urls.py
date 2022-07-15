from django.urls import path
from .views import *


urlpatterns = [
    path('', root ),
    path('index', index, name='index'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('apiSismos/', apiSismos, name='apiSismos'),
    path('productos/', productos, name='productos'),
    path('regContacto/',regContacto, name='regContacto'),
    path('registro/', registro, name='registro'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('success', success, name='success'),   
]