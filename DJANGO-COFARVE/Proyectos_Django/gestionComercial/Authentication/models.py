from django.db import models
from django.contrib.auth.models import AbstractUser, User, Group, Permission
from django.db.models.fields import CharField

#Agregamos la opción Perfiles a nuestro modelo
# Perfiles_users=[
#     ("Administrador", "Administrador"),
#     ("Supervisor", "Supervisor"),
# ]

# class Perfil(models.Model):
#     Perfil = models.CharField(max_length=20,choices=Perfiles_users,default="Administrador")

# Create your models here.
#Heredamos de la clase Usuario que viene por defecto en django y modificamos sus atributos
# class User(AbstractUser):
#     id_Perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,null=False,blank=False,default=1)

# class Perfil(models.Model):
#     nombre = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name
# Group.objects.create(name="Administrador",)


# permisos = Permission.objects.values()
# print(permisos)
# Authentication.add_user

administrador = Group.objects.get(name="Administrador")

# administrador.permissions.set([permisos.add_user, permisos.delete_user, permisos.view_user, permisos.change_user])


class Usuario(User):
        class Meta:
            proxy = True
        
        
    
    # """ nombre = models.CharField(max_length=200)
    # perfil = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)  """

