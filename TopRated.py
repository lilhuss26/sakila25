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
print(topRated_moviesID)

topRated_moviesData = {}
for movie_id in topRated_moviesID:
    movie_detailsURL = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    
    movie_details = requests.get(url=movie_detailsURL)
    movie_details_data = movie_details.json()

    film_id = movie_id
    title = movie_details_data["title"]
    description = movie_details_data["overview"]
    release_date = movie_details_data["release_date"]
    language = movie_details_data["original_language"]
    popularity = movie_details_data["popularity"]
    revenue = movie_details_data["revenue"]
    runtime = movie_details_data["runtime"]
    rating = movie_details_data["vote_average"]
    adult = movie_details_data["adult"]

    topRated_moviesData[film_id] = {
        "title":title,
        "rating":rating,
        "description":description,
        "release_date":release_date,
        "language":language,
        "popularity":popularity,
        "revenue":revenue,
        "runtime":runtime,
        "adult":adult
    }
movie_rate_df = pd.DataFrame.from_dict(topRated_moviesData, orient='index')
movie_rate_df = movie_rate_df.rename_axis('id')
movie_rate_df = movie_rate_df.reset_index()
movie_rate_df.to_csv("top_rated_movies.csv", index=False)
print(movie_rate_df.head())