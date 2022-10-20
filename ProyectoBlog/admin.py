from django.contrib import admin
from ProyectoBlog.models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Comment)

class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)
