from django.shortcuts import render

# Create your views here.
def hola(solicitud):
    return HttpResponse("¡Hola mundo!")