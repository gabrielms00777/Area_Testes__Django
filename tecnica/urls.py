from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel, name='painel'),
    path('os/', views.os, name='os'),
    path('clientes/', views.clientes, name='clientes'),
    path('pesquisa_cliente/', views.pesquisa_cliente, name='pesquisa_cliente')
]
