
from django import forms
from django.forms import ModelForm  
from .models import Contacto
from django.forms import ValidationError
import re

class ContactoFrom(ModelForm):

    #selector = forms.IntegerField(widget=forms.Select(attrs={"class":"col-11 form-control"}))
    rut = forms.CharField()
    nombre = forms.CharField(min_length=3 , max_length=100)
    correo = forms.EmailField()
    numero = forms.CharField()
    comentario = forms.CharField(required=False)
    condiciones = forms.BooleanField()



    class Meta:
        model = Contacto
        fields = ['rut','nombreCompleto','correo','numero','comentario','condiciones'
                ]
        
        labels = {'rut':'Rut:',
                'nombre':'Nombre:',
                'correo':'Correo Electronico:',
                'numero':'Numero:',
                'comentario':'Comentario:',
                'condiciones':'Terminos y Condiciones:'
                }
        widgets = { 'rut':forms.TextInput(attrs={"class":"col-sm-11 form-control", "placeholder":"12345678-9"}),
                    'nombre': forms.TextInput(attrs={"class":"form-control col-10 ","placeholder":"Juan"}), 
                    'correo':forms.EmailInput(attrs={"class":"col-sm-11 form-control", "placeholder":"nombre@gmail.com"}),
                    'numero':forms.TextInput(attrs={"class":"col-sm-11 form-control", "placeholder":"55667788"}),
                    'comentario':forms.Textarea(attrs={"class":"col-sm-11 form-control","placeholder":"Comentario"}),
                    'condiciones':forms.CheckboxInput(attrs={"class":"form-check-input"})

                }