from django import forms
from django.db import models
from django.db.models import fields
from .models import ComentarioContacto
from .models import Alumnos
from .models import AlumnoRegistro

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario','mensaje']

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['matricula','nombre','carrera','turno','imagen']

class AlumnoRegistroForm(forms.ModelForm):
    class Meta:
        model = AlumnoRegistro
        fields = ['matricula','nombre','imagen']