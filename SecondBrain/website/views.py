
from django.shortcuts import redirect, render
from .models import *
from django.conf import settings

    #the data here comes from the urls.py

# Create your views here.
def comming_soon(request):

    #for example here I send the e-mail to the template
    email = "kimmo.paananen@gmail.com"

    context = {
        # add here what you want to pass in to the template
    "email": email,
    }
    return render(request, 'comming-soon.html', context)
