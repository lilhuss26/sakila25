import os
import requests
from dotenv import load_dotenv
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

topurl = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&page=1&language=en-US"
topRated = requests.get(url=topurl)
topRated_data = topRated.json()
results = topRated_data.get("results")
movie_rate = {}
for movie in results:
    film_id = movie["id"]
    title = movie["title"]
    rate = movie["vote_average"]
    movie_rate[film_id] = {
        #"id":film_id,
        "title":title,
        "rate":rate
    }
#print(movie_rate)
movie_rate_df = pd.DataFrame.from_dict(movie_rate, orient='index')
movie_rate_df = movie_rate_df.rename_axis('id')
movie_rate_df = movie_rate_df.reset_index()
movie_rate_df.to_csv("top_rated_movies.csv", index=False)
print(movie_rate_df.head())