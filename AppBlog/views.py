from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from AppBlog.models import *

# Create your views here.

def cover (request):
    return render(request, 'cover.html')

def inicio(request):
    return render(request, 'padre.html')


def estudianteFormulario(request):

    if(request.method == 'POST'):
    
        estudiante = Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        estudiante.save()
        messages.success(request, '¡Estudiante agregado con éxito!')
        return render(request, 'forms/estudiante.html')



    return render(request, 'forms/estudiante.html')


def cursoFormulario(request):

    if(request.method == 'POST'):

        curso = Curso(nombre = request.POST['nombre'], camada = request.POST['camada'])
        curso.save()
        messages.success(request, '¡Curso agregado con éxito!')
        return render(request, 'forms/curso.html')


    return render(request, 'forms/curso.html')

def entregableFormulario(request):

    if(request.method == 'POST'):
        if(request.POST.get('enable') == None):
            entregable = Entregable(nombre = request.POST['nombre'], fechaDeEntrega = request.POST['fecha'], entregado = False)
        else:
            entregable = Entregable(nombre = request.POST['nombre'], fechaDeEntrega = request.POST['fecha'], entregado = request.POST['entregado'])
        entregable.save()
        messages.success(request, '¡Entregable agregado con éxito!')
        return render(request, 'forms/entregable.html')


    return render(request, 'forms/entregable.html')

def profesorFormulario(request):

    if(request.method == 'POST'):

        profesor = Profesor(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'], profesion = request.POST['profesion'])
        profesor.save()
        messages.success(request, '¡Profesor agregado con éxito!')
        return render(request, 'forms/profesor.html')


    return render(request, 'forms/profesor.html')


def busquedaCurso(request):

    return render(request, 'search_form_coder.html')

def buscar(request):

    if request.GET['camada']:

        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        object_name = 'Cursos'
        #respuesta = f"Estoy buscando la camada: {request.GET['camada']}"
        return render(request, 'search_results_coder.html', {"cursos": cursos, "camada": camada, "object_name": object_name})

    else:

        respuesta = 'No encontré nada mani :('

    return HttpResponse(respuesta)