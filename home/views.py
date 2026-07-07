

# Create your views here.

from django.shortcuts import render, redirect
from .models import Blog
from .models import HomeContent

from .models import Guestbook
from .forms import GuestbookForm


# I gonna change to make admin works btter code is correct but I need to have different one
"""
def home(request):
    content = HomeContent.objects.first()  # get latest/first entry
    return render(request, 'home/home.html', {'content': content})
"""
#  this is end of the change

# updated code STARTs here

def home(request):
    content = HomeContent.objects.all().order_by('-id')
    return render(request, 'home/home.html', {'content': content})


# uptaded code ENDS here

"""
def blog(request):
    return render(request, 'home/blog.html')
"""

def blog(request):
    posts = Blog.objects.all()
    return render(request, 'home/blog.html', {'posts': posts})


# here I will update the guestbook

def guestbook(request):
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')
    else:
        form = GuestbookForm()

    messages = Guestbook.objects.order_by('-created_at')

    return render(request, 'home/guestbook.html', {
        'form': form,
        'messages': messages
    })


# here updated the guestbook code will be ended

def contact(request):
    return render(request, 'home/contact.html')




"""
from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home/base.html')


  return HttpResponse(template.render())

"""