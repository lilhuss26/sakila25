import os
import requests
from dotenv import load_dotenv
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

top_ratedURL = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&page=1&language=en-US"
topRated = requests.get(url=top_ratedURL)
topRated_data = topRated.json()
results = topRated_data.get("results")
topRated_movies = {}
for movie in results:
    film_id = movie["id"]
    title = movie["title"]
    description = movie["overview"]
    release_date = movie["release_date"]
    language = movie["original_language"]
    rating = movie["vote_average"]
    topRated_movies[film_id] = {
        #"id":film_id,
        "title":title,
        "rating":rating,
        "description":description,
        "description":description,
        "language":language,
    }
movie_rate_df = pd.DataFrame.from_dict(topRated_movies, orient='index')
movie_rate_df = movie_rate_df.rename_axis('id')
movie_rate_df = movie_rate_df.reset_index()
movie_rate_df.to_csv("top_rated_movies.csv", index=False)
print(movie_rate_df.head())