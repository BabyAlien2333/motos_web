from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_motos, name='lista_motos'),
    path('moto/<int:id>/', views.detalle_moto, name='detalle_moto'),
    path('tasa-cambio/', views.tasa_cambio, name='tasa_cambio'),
    path('agregar-resena/<int:id>/', views.agregar_resena, name='agregar_resena'),
    path('registro/', views.registro, name='registro'),
]

