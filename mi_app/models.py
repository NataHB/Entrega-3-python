from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=40)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
