from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta Avatares de media
    image = models.ImageField(upload_to='avatares', null = True, blank = True)

# Acá agrego los campos extra para los usuarios

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    description = models.TextField(max_length=300)
    web_link = models.URLField()

def __str__(self):
    return self.user.username