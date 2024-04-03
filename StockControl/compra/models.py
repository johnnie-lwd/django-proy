from django.db import models

# Create your models here.

class Proveedor(models.Model):
    razonsoc=models.CharField(max_length=50)
    cuit=models.CharField(max_length=11)
    celular=models.CharField(max_length=9)
    def __str__(self):
        return self.razonsoc

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    stock_actual=models.IntegerField()
    proveedor=models.ForeignKey(Proveedor, on_delete = models.CASCADE )
    def __str__(self):
        return self.nombre