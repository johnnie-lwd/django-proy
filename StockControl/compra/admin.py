from django.contrib import admin
from .models import Producto, Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["razonsoc","cuit","celular"]

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "stock_actual","proveedor"]

# Register your models here.

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
