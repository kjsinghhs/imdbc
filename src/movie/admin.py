from django.contrib import admin

# Register your models here.

from .models import Movie,Watch_Link,Comment

admin.site.register(Movie)
admin.site.register(Watch_Link)
admin.site.register(Comment)