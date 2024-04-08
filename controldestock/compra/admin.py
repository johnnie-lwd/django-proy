from django.contrib import admin
from .models import Producto, Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'razonsoc', 'cuit', 'celular')
    search_fields = ('id', 'razonsoc', 'cuit', 'celular')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stockact', 'proveedor')
    search_fields = ('id', 'nombre', 'precio','stockact', 'proveedor' )

                     

# Register your models here.

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
