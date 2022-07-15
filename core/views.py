from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.contrib import messages
from crud.models import *
import bcrypt
from .models import *

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
    context = {'productos':Producto.objects.all()}
    return render(request, "core/productos.html",context)

def register(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        if request.method == 'POST':
            errors = User.objects.validador_campos(request.POST)

            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)

                #Si se produce un error pero no queremos perder los datos....
                request.session['registro_nombre'] = request.POST['first_name']
                request.session['registro_apellido'] = request.POST['last_name']
                request.session['registro_email'] = request.POST['email']
                request.session['level_mensaje'] = 'alert-danger'

            else:
                request.session['registro_nombre'] = ""
                request.session['registro_apellido'] = ""
                request.session['registro_email'] = ""

                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

                obj = User.objects.create(first_name=first_name, last_name=last_name,email=email,password=password_hash)
                messages.success(request, "Usuario registrado con éxito!!!!")
                request.session['level_mensaje'] = 'alert-success'
            
            return redirect('/registro')

        return render(request, 'registro')
            
            
def login(request):
    if request.method == 'GET':
        return redirect("/")
    else:
        if request.method == 'POST':
            
            user = User.objects.filter(email=request.POST['email_login']) #Buscamos el correo ingresado en la BD             
            
            if user : #Si el usuario existe

                usuario_registrado = user[0]
                
                if bcrypt.checkpw(request.POST['password_login'].encode(), usuario_registrado.password.encode()): 
                    usuario = {
                        'id':usuario_registrado.id,
                        'first_name':usuario_registrado.first_name,
                        'last_name':usuario_registrado.last_name,
                        'email':usuario_registrado.email,
                        'rol':usuario_registrado.rol,
                    }

                    request.session['usuario'] = usuario
                    messages.success(request,"Ingreso correcto!!!!")
                    return redirect('/success')
                else:
                    messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                    return redirect('/registro')
            else:
                messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                return redirect('/registro')
            
def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    
    return redirect('/')


def success(request):
    if 'usuario' not in request.session:
        return redirect('/')
        
    return render(request, 'core/success.html')

def registro(request):
    return render(request,"core/registro.html")

def regContacto(request):
    
    rut = request.POST['rut']
    nombre = request.POST['nombreCompleto']
    correo = request.POST['correo']
    numero = request.POST['numero']
    comentario = request.POST['comentario']
    condiciones = True

    formulario = Contacto.objects.create(
        nombre=nombre,numero=numero,rut=rut,
        correo=correo,comentario=comentario,condiciones=condiciones)
    formulario.save()
    return render(request,"core/contacto.html")