from django.contrib import admin
from django.urls import path
from . import views

# figure path here. This is sent to views.py


urlpatterns = [
    path('', views.comming_soon, name="comming_soon"),
]
