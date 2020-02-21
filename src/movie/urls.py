
from django.urls import path
from .views import MovieDetail, MovieList, MovieCategory,MovieSearch,MovieYear

app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(),name = 'movie_list'),
    path('category/<str:category>', MovieCategory.as_view(),name = 'movie_category'),
    path('search/', MovieSearch.as_view(),name = 'movie_search'),
    path('year/<int:year>', MovieYear.as_view(),name = 'movie_year'),
    path('<int:pk>', MovieDetail.as_view(),name = 'movie_detail'),
]


