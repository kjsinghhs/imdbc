from django.contrib import admin

# Register your models here.

from .models import Movie,Watch_Links,Commments

admin.site.register(Movie)
admin.site.register(Watch_Links)
admin.site.register(Commments)