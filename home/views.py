

# Create your views here.

from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def blog(request):
    return render(request, 'home/blog.html')

def guestbook(request):
    return render(request, 'home/guestbook.html')

def contact(request):
    return render(request, 'home/contact.html')




"""
from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home/base.html')


  return HttpResponse(template.render())

"""