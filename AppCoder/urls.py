from . import views
from django.urls import path

urlpatterns = [
    path('template/' , views.probandoTemplate),
    path('data/' , views.data),
    path('' , views.inicio, name="Inicio" ),
    path('curso' , views.curso, name="Curso" ),
    path('estudiante' , views.estudiante, name="Estudiante" ),
    path('profesor' , views.profesor, name="Profesor" ),
    path('entregable' , views.entregable, name="Entregable" ),

    
]

