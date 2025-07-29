from django.urls import path
from .views import TrendingMoviesView, MovieDetailView, TMDbRecommendationsView

urlpatterns = [
    path('trending/', TrendingMoviesView.as_view(), name='trending-movies'),
    path('<int:movie_id>/', MovieDetailView.as_view(), name='movie-detail'),
    path('recommendations/<int:movie_id>/', TMDbRecommendationsView.as_view(), name='movie_recommendations'),

]
