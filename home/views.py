

# Create your views here.

from django.shortcuts import render
from .models import Blog
from .models import HomeContent




def home(request):
    content = HomeContent.objects.first()  # get latest/first entry
    return render(request, 'home/home.html', {'content': content})





def blog(request):
    return render(request, 'home/blog.html')


def blog(request):
    posts = Blog.objects.all()
    return render(request, 'home/blog.html', {'posts': posts})

from .models import Guestbook

def guestbook(request):
    entries = Guestbook.objects.all()
    return render(request, 'home/guestbook.html', {'entries': entries})

def contact(request):
    return render(request, 'home/contact.html')




"""
from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home/base.html')


  return HttpResponse(template.render())

"""