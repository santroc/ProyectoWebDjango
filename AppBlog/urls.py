from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path('home', inicio, name='Inicio'),
    path('addEstudiante', estudianteFormulario, name='addEstudiante'),
    path('addCurso', cursoFormulario, name='cursoEstudiante'),
    path('addProfesor', profesorFormulario, name='cursoProfesor'),
    path('addEntregable', entregableFormulario, name='cursoEntregable'),
    path('searchCurso', busquedaCurso, name='busquedaCurso'),
    path('search/', buscar),
]