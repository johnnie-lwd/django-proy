from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from compra.models import Producto,Proveedor
from compra.forms import ProductoForm, ProveedorForm

# Create your views here.

#home
def index(request):
    doc_ext=open("C:/Users/juan.moyano/Desktop/Proyectos Django/controldestock/compra/templates/compra.html")
    plant=Template(doc_ext.read())
    doc_ext.close()
    context=Context()
    doc=plant.render(context)
    return HttpResponse(doc)

#listado de productos
def lista_prod(request):
    productos=Producto.objects.all()
    context={'productos': productos}
    return render(request,'compra/lista_prod.html',context)

#listado de proveedores
def lista_prov(request):
    proveedores=Proveedor.objects.all()
    context={'proveedores': proveedores}
    return render(request,'compra/lista_prov.html',context)