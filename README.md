# ProyectoWebDjango
Proyecto de curso Python + Django

Este proyecto tiene tres Apps.

Para ingresar a la página principal de la aplicación se podrá ingresar a:
    http://127.0.0.1:8000/cover
Desde dicho link se podrá acceder tanto a la aplicación AppBlog como al Blog. 

1. AppBlog: Una aplicación donde se encuentra lo que hemos venido trabajando en clase, modelos Estudiante, Profesor, Entregable, Curso con la posibilidad de agregar nuevos a través de de un formulario y poder buscar cursos por número de cursada (camada)

La URL base es la siguiente: http://127.0.0.1:8000/AppBlog/home

¡Proyecto Final!

Integrantes:

Santiago Troitiño Cristancho:

    - Desarrollo de Back-end para CRUD de Posts e implementación de módulo de User Management (Registro, logueo y funcionalidades exclusivas de usuarios registrados), también hice el Front-end.

Detalle de casos de QA: https://docs.google.com/spreadsheets/d/1gs2u9Oyg0yUvxJwAA5CTyFeL6eOY1IdVnP1bjuuwApM/edit#gid=0

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

Deben realizarse:

- Complementar modelo de "Post":
    - Agregar subtítulo, autor e imagen (X)
- Módulo de Usuarios Django: 
   - Mover todo lo relacionado a este módulo a una App independiente y respetar estructura de rutas de la entrga final (ejemplo: /accounts/xyz) (X)
   - Incluir la opción de editar: descripción  y un link a una página web (X)
        - Agregar mensaje de éxito al editar y atomicidad para la view de edición (X)
- Implementar página de About (X)
- Adaptar página para que ciertas funciones solo puedan realizarse con sesión iniciada:
   - Para crear, editar o borrar las fotos debes estar registrado como Administrador (X)
- Crear por lo menos tres casos de prueba documentados (X)
- Crear funcionalidad de mensajería entre perfiles:
    - Implementar funcionalidad de enviar mensajes a otros perfiles (X)
    - Implementar bandeja de entrada con mensajes ordenados del más a menos reciente (X)
    - Implementar botón de respuesta (X)

Opcionales despriorizados (Posterior a entrega final):
- Subir a Heroku ()
- Revisar cómo corregir la visualización de mensajes de error (Que se muestren en rojo en vez de verde como los de success) ()
- Solucionar bug donde ciertas views redireccionan a la página principal pero no se ve el avatar ()
- Agregar foto de perfil predeterminada ()
