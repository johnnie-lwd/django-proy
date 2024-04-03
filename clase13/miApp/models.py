from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100,
                blank = True,
                null = True)
    categoria=models.CharField(max_length=100,
                               default = "Sin categoria")
    color=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=10,decimal_places=2,
                               default = 0)
    