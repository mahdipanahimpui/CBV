from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='home'), 
    # path('two/', views.Two.as_view(), name='two'),
    # path('<int:pk>', views.CarDetailView.as_view(), name='car_detail'), # <int:pk> not id
    # path('create/', views.CarCreateView.as_view(), name='car_create'),
    path('delete/<int:pk>/', views.CarDeleteView.as_view(), name='car_delete'),
    path('update/<int:pk>/', views.CarupdateView.as_view(), name='car_update'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('<int:year>/<int:month>', views.MonthCarView.as_view(), name='car_month')
]