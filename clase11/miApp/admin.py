from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["titulo","descripcion","categoria","color","precio"] #establecer que campos mostrar
    search_fields = ["titulo","descripcion","categoria","color","precio"]

# Register your models here.
admin.site.register(Producto, ProductoAdmin)