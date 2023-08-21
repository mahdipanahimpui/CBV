from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='home'), 
    # path('two/', views.Two.as_view(), name='two'),
    # path('<int:pk>', views.CarDetailView.as_view(), name='car_detail'), # <int:pk> not id
    # path('create/', views.CarCreateView.as_view(), name='car_create'),
    path('delete/<int:pk>/', views.CarDeleteView.as_view(), name='car_delete')
]