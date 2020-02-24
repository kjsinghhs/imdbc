from django.db import models
import datetime 
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.

CATEGORY_CHOICES = {
    ('action','ACTION'),
    ('drama','DRAMA'),
    ('comedy','COMEDY'),
    ('romance','ROMANCE'),
}

STATUS_CHOICES = {
    ('tr','Top Rated'),
    ('ra','Recently Added'),
    ('mw','Most Watched'),
}

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 2000)
    image = models.ImageField(upload_to = 'movie')
    category = models.CharField(choices = CATEGORY_CHOICES,max_length = 10)
    cast = models.CharField(max_length=100)
    year_of_production =  models.DateField()
    views_count = models.IntegerField(default = 0)
    slug = models.SlugField(blank = True , null=True)
    movie_trailer = models.URLField()
    created = models.DateTimeField(default = timezone.now, auto_now=False, auto_now_add=False)
    status = models.CharField(choices = STATUS_CHOICES, max_length=2)

    #Overide the Save method to slugify the movie for better searching.
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug =  slugify(self.title)
        super(Movie,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class Watch_Link(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    link = models.URLField(max_length=200)

    def __str__(self):
        return str(self.movie)


class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_comment', on_delete=models.CASCADE)
    comment = models.TextField()
    created_on  = models.DateTimeField(default = timezone.now)
    userid =  models.IntegerField(default = 0)
    username = models.CharField(max_length=100)
    slug = models.SlugField(blank = True , null=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug =  slugify(self.movie)
        super(Comment,self).save(*args,**kwargs)

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.username)

    # def comment_posted(self):
    #     comment_movie = self.movie
    #     comment_data = comment.objects.filter_    

# class Comment(models.Model):
#     post = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='comments')
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     # active = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body, self.name)