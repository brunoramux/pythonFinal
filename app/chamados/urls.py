from django.contrib import admin
from django.urls import path
from chamados import views

urlpatterns = [
    path('', views.ChamadoList.as_view(), name='chamadoList'),
    path('create/', views.ChamadoCreate.as_view(), name='create')
]