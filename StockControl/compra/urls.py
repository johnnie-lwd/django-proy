from django.urls import path
from . import views

urlpatterns = [
    path('compra/proveedores', views.listaprov),
    path('compra/productos', views.listaprod),
    path('compra/formprov', views.formpv),
    path('compra/formprod', views.formpd),
    path('', views.compra),
    
]