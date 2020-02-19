from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Movie , Watch_Links , Commments


class MovieList(ListView):
    model = Movie
    paginate_by = 1
    # template_name = ".html"


class MovieDetail(DetailView):
    model = Movie
    # template_name = ".html"

    def get_object(self):
        pass

    def get_comment(self):
        pass
