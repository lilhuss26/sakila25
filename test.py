import os
import requests
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
movie_response = requests.get(f"https://api.themoviedb.org/3/movie/640?api_key={TMDB_API_KEY}")
print(movie_response.text)