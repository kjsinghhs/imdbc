from django.db import models
import datetime

# Create your models here.

CATEGORY_CHOICES = {
    ('A','ACTION'),
    ('D','DRAMA'),
    ('C','COMEDY'),
    ('R','ROMANCE'),
}

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 2000)
    image = models.ImageField(upload_to = 'movie')
    category = models.CharField(choices = CATEGORY_CHOICES,max_length = 1)
    # language = models.CharField(choices = LANGUAG)
    cast = models.CharField(max_length=100)
    year_of_production =  models.DateField()
    views_count = models.IntegerField(default = 0)


    def __str__(self):
        return self.title

class Watch_Links(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    link = models.URLField(max_length=200)

    def __str__(self):
        return str(self.movie)


class Commments(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_comment', on_delete=models.CASCADE)
    comment = models.CharField(max_length=5000)
    userid =  models.IntegerField(default = 0)
    username = models.CharField(max_length=100)

    def __str__(self):
        return str(self.movie)
    