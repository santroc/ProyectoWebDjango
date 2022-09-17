from django.shortcuts import render
from django.contrib import messages
from AppBlog.models import *

# Create your views here.


def inicio(request):

    return render(request, 'padre.html')


def cursoFormulario(request):

    if(request.method == 'POST'):

        curso = Curso(nombre = request.POST['nombre'], camada = request.POST['camada'])
        curso.save()
        messages.success(request, '¡Curso agregado con éxito!')
        return render(request, 'forms/curso.html')


    return render(request, 'forms/curso.html')

def profesorFormulario(request):

    if(request.method == 'POST'):

        profesor = Profesor(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'], profesion = request.POST['profesion'])
        profesor.save()
        messages.success(request, '¡Profesor agregado con éxito!')
        return render(request, 'forms/profesor.html')


    return render(request, 'forms/profesor.html')