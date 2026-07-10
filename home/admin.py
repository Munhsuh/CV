

# Register your models here.

from django.contrib import admin
from .models import Blog, Guestbook, HomeContent, Contact

admin.site.register(Blog)
admin.site.register(Guestbook)
admin.site.register(HomeContent)
admin.site.register(Contact)

