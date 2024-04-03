from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
cursos=[
    {"titulo": "HTML y CSS","descripcion": "maquet web"}, 
    {"titulo": "javascript","descripcion": "javabla"},
    {"titulo": "tornillo","descripcion": "tornibla"},
    {"titulo": "asado","descripcion": "cociname"}
]

def salu(request):
    nombre="juan"
    ruta="C:/Users/juan.moyano/Desktop/Proyectos Django/clase12/miApp/templates/salu.html"
    doc_externo=open(ruta)
    plant=Template(doc_externo.read())
    doc_externo.close()
    contexto=Context({"nombre":nombre, "cursos":cursos})
    doc=plant.render(contexto)
    return HttpResponse(doc)
