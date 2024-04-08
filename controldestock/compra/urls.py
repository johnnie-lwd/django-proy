from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compra/proveedores', views.lista_prov, name='Proveedores'),
    
   
]