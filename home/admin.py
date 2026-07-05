

# Register your models here.


from django.contrib import admin
from .models import Blog, Guestbook
from .models import HomeContent

admin.site.register(Blog)
admin.site.register(Guestbook)
admin.site.register(HomeContent)