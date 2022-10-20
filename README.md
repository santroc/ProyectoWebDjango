# ProyectoWebDjango
Proyecto de curso Python + Django

Este proyecto tiene tres Apps.

Para ingresar a la página principal de la aplicación debe utilizar el siguiente link:
    http://127.0.0.1:8000/

Desde dicho link se accederá a la portada, de allí se puede acceder tanto a la aplicación AppBlog como al Blog. 

1. AppBlog: Una aplicación donde se encuentra lo que hemos venido trabajando en clase, modelos Estudiante, Profesor, Entregable, Curso con la posibilidad de agregar nuevos a través de de un formulario y poder buscar cursos por número de cursada (camada)

La URL base es la siguiente: http://127.0.0.1:8000/AppBlog/home

¡Proyecto Final!

Integrantes:

Santiago Troitiño Cristancho:

    - Desarrollo de Back-end para CRUD de Posts, módulo de mensajería y de User Management (Registro, logueo y funcionalidades exclusivas de usuarios registrados), también hice el Front-end.

Detalle de casos de QA: https://docs.google.com/spreadsheets/d/1gs2u9Oyg0yUvxJwAA5CTyFeL6eOY1IdVnP1bjuuwApM/edit#gid=0

Tatiana Cazzazola:

    - Página Front-End de portada, Front-End del Blog. Creación de módulo para posteo de comentarios

2. ProyectoBlog:

Acá se encuentra todo el trabajo que se ha desarrollado referente al proyecto de creación de un Blog.

La URL base es la siguiente: http://127.0.0.1:8000/pages/

Para agregar una nueva entrada: Seleccionar en la nav-bar "Nuevo post"

Para buscar Posts por título seleccionar "Buscar Post" en la nav-bar

En la pantalla de home se irán listando las diferentes entradas las cuales son listadas de la más reciente a la más antigua, cada una de ellas cuenta con la opción de ver a detalle ("Leer más") Editar la entrada o eliminarla.

3. UserManagement:

Acá se encuentra todo el trabajo que se encarga de registro, creación y edición de usuarios, las páginas relacionadas a este módulo usan la siguiente estructura de URL:

http://127.0.0.1:8000/accounts/(...)


Pendientes:
- Incluir la opción de editar: descripción  y un link a una página web (X)
    - Agregar mensaje de éxito al editar y atomicidad para la view de edición (X)
- Aprobar automáticamente comentarios en caso de ser un usuario registrado.

Opcionales despriorizados (Posterior a entrega final):
- Subir a Heroku (X)
- Revisar cómo corregir la visualización de mensajes de error (Que se muestren en rojo en vez de verde como los de success) ()
- Revisar error de edición de perfil para usuarios que no tengan uno creado ()
- Solucionar bug donde ciertas views redireccionan a la página principal pero no se ve el avatar ()
- Agregar foto de perfil predeterminada ()
