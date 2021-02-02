from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index , name='home'),
    path('about/', views.about , name='about'),
    path('home/', views.home , name='myhome'),
    path('services/', views.services , name='services'),
    path('contact/', views.contact , name='mycontact'),
    path('order/', views.order , name='myorder'),
]