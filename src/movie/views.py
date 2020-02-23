from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie , Watch_Link , Comment

#TODO: Adding the Home view for the website.
class HomeView(ListView):
    model = Movie
    template_name  = 'movie/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='tr')
        context['recently_added'] = Movie.objects.filter(status='ra')
        context['most_watched'] = Movie.objects.filter(status='mw')
        
        return context
    

#TODO: Creating a MovieListing which is used to show the list of movies based on the headers
class MovieList(ListView):
    model = Movie
    paginate_by = 2

#TODO: Creating a Movie Details Page to be viewed by the user once a Movie is clicked
class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail,self).get_context_data(**kwargs)
        context["links"] = Watch_Link.objects.filter(movie=self.get_object())
        context["comments"] = Comment.objects.filter(movie=self.get_object())
        context["related_movies"] = Movie.objects.filter(category=self.get_object().category)#.order_by['created'][0:6]
        print(context)
        return context

#TODO: Creating a MovieList view based on the Category.
class MovieCategory(ListView):
    model = Movie
    paginate_by = 2

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category = self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory,self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context
    
#TODO: Creating a Search bar entries
class MovieSearch(ListView):
    model = Movie
    paginate_by =  2

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains = query)
        else:
            object_list = self.model.objects.none()
        return object_list

#TODO: Creating a MovieList view based on the Year.
class MovieYear(YearArchiveView):

    queryset = Movie.objects.all()
    date_field =  'year_of_production'
    make_object_list = True
    allow_future = True


#TODO: Creating a comment section for the user.

class MovieComment(ListView):
    model = Comment

    def get_queryset(self):
        self.movie = self.kwargs['category']
        return Movie.objects.filter(category = self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory,self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context
    

    
        
