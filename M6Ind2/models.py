from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)