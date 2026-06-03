from django.contrib import admin
from django.urls import path
from . import views

# figure path here. This is sent to views.py


urlpatterns = [
    path('', views.home, name='home'),
    path('tapahtumat/', views.events, name='events'),
    path('ajankohtaista/', views.blog, name='blog'),
    path('kuvagalleria/', views.gallery, name='gallery'),
    path('yhteystiedot/', views.contact, name='contact'),
]
