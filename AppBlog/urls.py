from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path('home', inicio, name='Inicio'),
    path('addCurso', cursoFormulario, name='cursoEstudiante'),
    path('addProfesor', profesorFormulario, name='cursoProfesor'),
]