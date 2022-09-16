from django.shortcuts import render
from django.contrib import messages
from AppBlog.models import *

# Create your views here.


def inicio(request):

    return render(request, 'padre.html')


def estudianteFormulario(request):

    if(request.method == 'POST'):
    
        estudiante = Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        estudiante.save()
        #return messages.success(request, 'Estudiante agregado con éxito')
        return render(request, 'padre.html')



    return render(request, 'forms/estudiante.html')