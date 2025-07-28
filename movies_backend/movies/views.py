from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils.tmdb import get_trending_movies, get_movie_details

class TrendingMoviesView(APIView):
    def get(self, request):
        movies = get_trending_movies()
        return Response(movies)

class MovieDetailView(APIView):
    def get(self, request, movie_id):
        try:
            movie = get_movie_details(movie_id)
            return Response(movie)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
