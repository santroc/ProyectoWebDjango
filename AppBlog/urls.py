from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path('home', inicio, name='Inicio'),
    path('addCurso', cursoFormulario, name='cursoEstudiante'),
    path('addProfesor', profesorFormulario, name='cursoProfesor'),
<<<<<<< HEAD
=======
    path('addEntregable', entregableFormulario, name='cursoEntregable'),
    path('searchCurso', busquedaCurso, name='busquedaCurso'),
    path('search/', buscar),
>>>>>>> experimental
]