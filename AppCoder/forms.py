from django import forms 


class CursoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class EstudianteForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class ProfesorForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class EntregableForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()  
    entregado = forms.BooleanField()