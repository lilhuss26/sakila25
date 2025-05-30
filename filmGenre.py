import os
import requests
from dotenv import load_dotenv
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")


topRated_moviesID = []
for i in range(1,6):
    top_ratedURL = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&page={i}&language=en-US"
    topRated = requests.get(url=top_ratedURL)
    topRated_data = topRated.json()
    results = topRated_data.get("results")
    for movie in results:
        film_id = movie["id"]
        topRated_moviesID.append(film_id)

topRated_moviesData = {}
for movie_id in topRated_moviesID:
    movie_detailsURL = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    
    movie_details = requests.get(url=movie_detailsURL)
    movie_details_data = movie_details.json()

    film_id = movie_id
    genre = movie_details_data["genres"][0]["id"]
    topRated_moviesData[film_id] = {
        "category_id":genre }
movie_rate_df = pd.DataFrame.from_dict(topRated_moviesData, orient='index')
movie_rate_df = movie_rate_df.rename_axis('film_id')
movie_rate_df = movie_rate_df.reset_index()
movie_rate_df.to_csv("Sakila_csv/film_category.csv", index=False)
print(movie_rate_df.head())