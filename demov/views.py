from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'home.html')



def About(request):
    return render(request, 'about.html')




def Contact(request):
    return render(request, 'contact.html')


def Gallery(request):
    return render(request, 'gallery.html')


def Service(request):
    return render(request, 'service.html')


def Form(request):
    return render(request, 'form.html')