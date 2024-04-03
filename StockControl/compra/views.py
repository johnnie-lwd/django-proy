from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .models import Proveedor,Producto

# Create your views here.

def listaprov(request):
    prov=Proveedor.objects.all()
    doc_ext1=open('C:/Users/juan.moyano/Desktop/Proyectos Django/StockControl/compra/templates/listadoprov.html')
    plant1=Template(doc_ext1.read())
    doc_ext1.close()
    contex1=Context({"proveedores":prov})
    doc1=plant1.render(contex1)
    return HttpResponse(doc1)

def listaprod(request):
    prod=Producto.objects.all()
    doc_ext2=open("C:/Users/juan.moyano/Desktop/Proyectos Django/StockControl/compra/templates/listadoprod.html")
    plant2=Template(doc_ext2.read())
    doc_ext2.close()
    contex2=Context({"productos":prod})
    doc2=plant2.render(contex2)
    return HttpResponse(doc2)

def compra(request):
    doc_ext3=open("C:/Users/juan.moyano/Desktop/Proyectos Django/StockControl/compra/templates/compra.html")
    plant3=Template(doc_ext3.read())
    doc_ext3.close()
    contex3=Context()
    doc3=plant3.render(contex3)
    return HttpResponse(doc3)

def formpv(request):
    doc_ext4=open("C:/Users/juan.moyano/Desktop/Proyectos Django/StockControl/compra/templates/formprov.html")
    plant4=Template(doc_ext4.read())
    if request.POST:
        rsoc=request.POST['rsoc']
        cuit=request.POST['cuit']
        celular=request.POST['celular']
        Proveedor.objects.create(rsoc=rsoc,cuit=cuit,celular=celular)
        return redirect('listaprov')
    
    doc_ext4.close()
    contex4=Context()
    doc4=plant4.render(contex4)
    return render(request,'compra/formprov.html')
    return HttpResponse(doc4)

def formpd(request):
    doc_ext5=open("C:/Users/juan.moyano/Desktop/Proyectos Django/StockControl/compra/templates/formprod.html")
    plant5=Template(doc_ext5.read())
    doc_ext5.close()
    contex5=Context()
    doc5=plant5.render(contex5)
    proveedor= Proveedor.objects.all()
    context={'proveedor': proveedor}
    if request.POST:
        nombre=request.POST['nombre']
        precio=request.POST['precio']
        stockact=request.POST['stockact']
        proveedor=request.POST['proveedor']
        Producto.objects.create(nombre=nombre,precio=precio,stockact=stockact,proveedor=proveedor)
        return redirect('listaprod')
    return render(request,'compra/formprod.html',context)
    return HttpResponse(doc5)


"""def formprov(request):
    if request.POST:
        rsoc=request.POST['rsoc']
        cuit=request.POST['cuit']
        celular=request.POST['celular']
        Proveedor.objects.create(rsoc=rsoc,cuit=cuit,celular=celular)
        return redirect('listaprov')
    return render(request,'compra/formprov.html')"""

"""def formprod(request):
    proveedor= Proveedor.objects.all()
    context={'proveedor': proveedor}
    if request.POST:
        nombre=request.POST['nombre']
        precio=request.POST['precio']
        stockact=request.POST['stockact']
        proveedor=request.POST['proveedor']
        Producto.objects.create(nombre=nombre,precio=precio,stockact=stockact,proveedor=proveedor)
        return redirect('listaprod')
    return render(request,'compra/formprod.html',context)
        """

