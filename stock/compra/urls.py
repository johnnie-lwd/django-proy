from django.urls import path
from . import views

urlpatterns = [
    path('', views.compra, name='home'),
    path('lista_prov/', views.lista_prov, name='lista_prov'),
    path('lista_prod/', views.lista_prod, name='lista_prod'),
    path('formpv/', views.formpv, name='formpv'),
    path('formpd/', views.formpd, name='formpd'),
]