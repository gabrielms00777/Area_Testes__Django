from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel, name='painel'),
    path('os/', views.os, name='os'),
    path('clientes/', views.clientes, name='clientes'),
    path('pesquisa_cliente/', views.pesquisa_cliente, name='pesquisa_cliente'),
    path('editar_cliente/<int:id>', views.editar_cliente, name='editar_cliente'),
    path('deletar_cliente/<int:id>', views.deletar_cliente, name='deletar_cliente'),
]
