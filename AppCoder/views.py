from distutils.log import info
import email
from logging.config import dictConfig
from tkinter import E
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader , Template , Context
from AppCoder.models import Curso, Estudiante, Profesor , Entregable
from .forms import CursoFormulario , EntregableForm , EstudianteForm, ProfesorForm

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

def cursoFormulario(request):

    # var = True

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            curso = Curso(nombre=informacion['nombre'] , camada = informacion['camada'])

            curso.save()
            return render(request, "AppCoder/inicio.html")
    else: 
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html" , {"miFormulario":miFormulario} )

def entregableFormulario(request):

    if request.method == 'POST':

        miFormulario = EntregableForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            entregable = Entregable(nombre=informacion['nombre'] , fechaDeEntrega = informacion['fechaDeEntrega'] , entregado = informacion['entregado'])

            entregable.save()

            return render(request, "AppCoder/inicio.html")

    else: 
        miFormulario = EntregableForm()
        
    
    return render(request, "AppCoder/entregableForm.html" , {"miFormulario" :miFormulario} )

def estudianteFormulario(request):

    if request.method == "POST":

        miFormulario = EstudianteForm(request.POST)

        print(miFormulario)
    
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            estudiante = Estudiante(nombre=informacion['nombre'] , apellido = informacion['apellido'] , email = informacion['email'])

            estudiante.save()


            
            return render(request , "AppCoder/inicio.html")

    else: 
        miFormulario = EstudianteForm()
        
    
    return render(request, "AppCoder/estudianteForm.html" , {"miFormulario" :miFormulario} )

def profesorFormulario(request):

    if request.method == 'POST':

        miFormulario = ProfesorForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre=informacion['nombre'] , apellido = informacion['apellido'] , email = informacion['email'] , profesion = informacion['profesion'])

            profesor.save()

            return render(request, "AppCoder/inicio.html")

    else: 
        miFormulario = ProfesorForm()
        
    
    return render(request, "AppCoder/profesorForm.html" , {"miFormulario" :miFormulario} )

def add(request):


    val1 = int(request.POST.get('num1' , False))
    val2 = int(request.POST.get('num2' , False))

    res = val1 + val2

    return render(request, "add.html" , {"res" : res})

def busquedaCamada(request):
    return render(request, "AppCoder/buscarCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        nombre = Curso.objects.filter(camada__icontains = camada)

        return render(request, "AppCoder/resultadoBusqueda.html" , {"camada":camada , "nombre": nombre})
    else:
        respuesta =  "No enviaste datos"

    return HttpResponse(respuesta)