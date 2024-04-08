from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.views.generic import (CreateView)
from .forms import ProductoForm,ProveedorForm
from .models import Producto,Proveedor

# Create your views here.

#home
def compra(request):
    doc_ext=open("C:/Users/juan.moyano/Desktop/Proyectos Django/stock/compra/templates/compra.html")
    plant=Template(doc_ext.read())
    doc_ext.close()
    doc=plant.render(Context())
    return HttpResponse(doc)

#lista proveedores
def lista_prov(request):
    proveedor = Proveedor.objects.all()
    return render(request, 'lista_prov.html', {'proveedor': proveedor})

#lista productos
def lista_prod(request):
    producto=Producto.objects.all()
    return render(request, 'lista_prod.html', {'producto': producto})

#form nuevo prov
def formpv(request):
    if request.POST:
        razonsoc=request.POST['razonsoc']
        cuit=request.POST['cuit']
        celular=request.POST['celular']
        Proveedor.objects.create(razonsoc=razonsoc,cuit=cuit,celular=celular)
        return redirect('lista_prov')
    return render(request, 'formpv.html')

#form nuevo prod
def formpd(request):
    proveedores=Proveedor.objects.all()
    context={'proveedores':proveedores}
    if request.POST:
        nombre=request.POST.get('nombre')
        precio=request.POST.get('precio')
        stockact=request.POST.get('stockact')
        proveedor_id=request.POST.get('proveedor')
        Producto.objects.create(nombre=nombre,precio=precio,stockact=stockact,proveedor_id=proveedor_id)
        return redirect('lista_prod')
    return render(request, 'formpd.html',context)