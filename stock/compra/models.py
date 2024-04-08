from django.db import models

# Create your models here.
#proveedor
class Proveedor(models.Model):
    razonsoc=models.CharField(max_length=50)
    cuit=models.CharField(max_length=50)
    celular=models.CharField(max_length=11)
    def __str__(self):
        return self.razonsoc
    

#producto
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.FloatField(max_length=10)
    stockact=models.IntegerField()
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre