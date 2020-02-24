
from django.urls import path
from .views import MovieDetail, MovieList, MovieCategory,MovieSearch,MovieYear,comment_details,CommentForm
from . import views

app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(),name = 'movie_list'),
    path('category/<str:category>', MovieCategory.as_view(),name = 'movie_category'),
    path('search/', MovieSearch.as_view(),name = 'movie_search'),
    path('year/<int:year>', MovieYear.as_view(),name = 'movie_year'),
    path('<slug:slug>', MovieDetail.as_view(),name = 'movie_detail'),
    path('movies/<slug:slug>', views.comment_details, name='comment_details'),
    path('movies/CommentForm', views.CommentForm, name='CommentForm'),
]


