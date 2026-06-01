from django.contrib import admin
from django.urls import path
from . import views

# figure path here. This is sent to views.py


urlpatterns = [
    path("", views.home, name="home"),
    path("events/", views.events, name="events"),
    path("blog/", views.blog, name="blog"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
]
