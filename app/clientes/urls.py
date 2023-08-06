from django.contrib import admin
from django.urls import path
from clientes import views

urlpatterns = [
    path('', views.ClienteList.as_view(), name='index'),
    path('create/', views.ClienteCreate.as_view(), name='create')
]