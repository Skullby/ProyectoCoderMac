from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('template/' , views.probandoTemplate),
    path('data/' , views.data),
    path('' , views.inicio, name="Inicio" ),
    path('curso/' , views.curso, name="Curso" ),
    path('estudiante/' , views.estudiante, name="Estudiante" ),
    path('profesor/' , views.profesor, name="Profesor" ),
    path('entregable/' , views.entregable, name="Entregable" ),
    path('cursoFormulario/', views.cursoFormulario , name = 'cursoFormulario'),
    path('estudianteForm/', views.estudianteFormulario , name = 'estudianteForm'),
    path('profesorForm/', views.profesorFormulario , name = 'profesorForm'),
    path('entregableForm/', views.entregableFormulario , name = 'entregableForm'),
    path('add/' , views.add , name = 'add'),
    path('busquedaCamada/' , views.busquedaCamada , name="busquedaCamada"),
    path('buscar/', views.buscar)

    
]

