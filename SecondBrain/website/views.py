
from django.shortcuts import redirect, render

from .models import *
from django.conf import settings



def home(request):
    return render(request, "index.html")


def events(request):
    return render(request, "events.html")


def blog(request):
    return render(request, "blog.html")


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    return render(request, "contact.html")
