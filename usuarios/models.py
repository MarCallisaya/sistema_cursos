from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    #tuplas, estas no se pueden modificar
    ROLES = (
        #tuplas
        ('administrador','Administrador'),
        ('profesor','Profesor'),
        ('estudiante','Estudiante'),
    )

    rol = models.CharField(max_length=30, choices=ROLES, default='estudiante')

    def __str__(self):
        return f"{self.username} - {self.rol}"

#creamos las demas tablas 
#Tablas para estudiante, profesor, administrador