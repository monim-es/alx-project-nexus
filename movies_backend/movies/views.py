from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils.tmdb import get_trending_movies, get_movie_details
import requests
from django.conf import settings


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


class TMDbRecommendationsView(APIView):
    def get(self, request, movie_id):
        api_key = settings.TMDB_API_KEY
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"
        params = {
            "api_key": api_key,
            "language": "en-US",
            "page": 1,
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if data["results"]:
                return Response(data["results"], status=200)
            else:
                return Response({"message": "No recommendations found for this movie."}, status=200)
        else:
            return Response({"error": "Failed to fetch recommendations from TMDb."}, status=500)
