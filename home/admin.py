

# Register your models here.

from django.contrib import admin
from .models import Blog, Guestbook, HomeContent, Contact
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(HomeContent)
class HomeContentAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)



admin.site.register(Guestbook)
admin.site.register(Contact)


