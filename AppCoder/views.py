from logging.config import dictConfig
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader , Template , Context
from .models import Curso, Estudiante, Profesor , Entregable

# Create your views here.
def probandoTemplate(self):
    nombre = "Juancito"
    ap = "Cucc"

    diccionario = {"nombre":nombre , "apellido":ap}

    plantilla = loader.get_template('padre.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def data(self):
    
    hola = "Hola"
    diccionario = {"Hola":hola}

    plantilla = loader.get_template('curso.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def curso(self):

    plantilla = loader.get_template('curso.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def estudiante(self):

    plantilla = loader.get_template('estudiantes.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def profesor(self):

    plantilla = loader.get_template('profesor.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def entregable(self):

    plantilla = loader.get_template('entregable.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def inicio(self):
    plantilla = loader.get_template('padre.html')
    documento = plantilla.render()

    return HttpResponse(documento)