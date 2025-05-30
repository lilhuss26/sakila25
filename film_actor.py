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

film_actor = []
actor = {}
for movie_id in topRated_moviesID:

    creditsURL = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=en-US"
    credits = requests.get(url=creditsURL)
    credits_data = credits.json()
    film_id = movie_id
    main_actor = credits_data['cast'][0]
    main_actor_id = main_actor['id']
    main_actor_name = main_actor['name']
    name_parts = main_actor_name.split()
    first_name = name_parts[0] if len(name_parts) > 0 else ""
    last_name = name_parts[1] if len(name_parts) > 1 else ""
    actor[main_actor_id]={
        "first_name" : first_name,
        "last_name" : last_name
    }
    film_actor.append({
            "actor_id": main_actor_id,
            "film_id": movie_id
        })
actor_df = pd.DataFrame.from_dict(actor, orient='index')
actor_df = actor_df.rename_axis('actoe_id')
actor_df = actor_df.reset_index()
actor_df.to_csv("Sakila_csv/actor.csv", index=False)
print(actor_df.head())
film_actor_df = pd.DataFrame(film_actor)
film_actor_df.to_csv("Sakila_csv/film_actor.csv", index=False)