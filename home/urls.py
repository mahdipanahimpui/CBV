from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='home'), 
    # path('two/', views.Two.as_view(), name='two'),
]