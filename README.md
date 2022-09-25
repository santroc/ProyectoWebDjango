# ProyectoWebDjango
Proyecto de curso Python + Django

Este proyecto tiene dos Apps.

1. AppBlog: Una aplicación donde se encuentra lo que hemos venido trabajando en clase, modelos Estudiante, Profesor, Entregable, Curso con la posibilidad de agregar nuevos a través de de un formulario y poder buscar cursos por número de cursada (camada)

La URL base es la siguiente: http://127.0.0.1:8000/AppBlog/home

2. ProyectoBlog:

Acá se encuentra todo el trabajo que se ha desarrollado referente al proyecto de creación de un Blog.

La URL base es la siguiente: http://127.0.0.1:8000/pages/home

Para agregar una nueva entrada: Seleccionar en la nav-bar "Nuevo post"

Para buscar Posts por título seleccionar "Buscar Post" en la nav-bar

En la pantalla de home se irán listando las diferentes entradas las cuales son listadas de la más reciente a la más antigua, cada una de ellas cuenta con la opción de ver a detalle ("Leer más") Editar la entrada o eliminarla.


Pendientes:

- Complementar modelo de "Post"
- Implementar módulo de Usuarios Django: Módulo básico implementado, pendiente revisar el Front-end para login, logout y registro, funcionan bien pero visualmente les falta trabajo.
- Adaptar página para que ciertas funciones solo puedan realizarse con sesión iniciada
- Revisar cómo corregir la visualización de mensajes de error (Que se muestren en rojo en vez de verde como los de success)
