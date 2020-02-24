from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie , Watch_Link ,Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django import forms

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
    paginate_by = 4

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
        return context

def comment_details(request,slug):
    template_name = 'movie/comments.html'
    movie = get_object_or_404(Movie,slug = slug)
    comment = Movie.comment.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        # Create Comment object but don't save to database yet
        new_comment = comment_form.save(commit=False)
        # Assign the current post to the comment
        new_comment.post = movie
        # Save the comment to the database
        new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': movie,
                                            'comments': comment,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form})



#TODO: Creating a MovieList view based on the Category.
class MovieCategory(ListView):
    model = Movie
    paginate_by = 4

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
    paginate_by =  4

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username', 'comment')

    def add_comment_to_post(request, pk):
        movie_to_comment = get_object_or_404(Movie, title=title)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'blog/add_comment_to_post.html', {'form': form})


    
        
