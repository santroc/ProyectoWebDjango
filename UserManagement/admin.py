from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Avatar)


#Clase para incluir en panel de admin nuevos atributos

class UserProfileInline(admin.StackedInline):
    model = PerfilUsuario #Modelo del que quiero agregar mis campos
    can_delete = False #Restringir el borrado a menos que sea en cascada desde el usuario
    verbose_name_plural = 'Profiles'

class CustommisedUserAdmin (UserAdmin):
    inlines = (UserProfileInline, )

#Quitamos el User que viene por defecto y agregamos con nuestra extensión del modelo

admin.site.unregister(User)
admin.site.register(User, CustommisedUserAdmin)