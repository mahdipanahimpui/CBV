from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('<str:name>/<int:id>/', views.Home.as_view(), name='home'), 
    path('two/<str:name>/<int:id>/', views.Two.as_view(), name='two')
]