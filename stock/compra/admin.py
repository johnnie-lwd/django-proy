from django.contrib import admin
from .models import Producto,Proveedor

# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id','razonsoc','cuit','celular')
    search_fields = ('razonsoc','cuit','celular')
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','precio','stockact','proveedor')
    search_fields = ('nombre','precio','stockact','proveedor')

admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Producto,ProductoAdmin)