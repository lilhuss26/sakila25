import os
import requests
from dotenv import load_dotenv
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def topRated_movies():
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
            "language_iso_639_1":language,
            "popularity":popularity,
            "revenue":revenue,
            "runtime":runtime,
            "adult":adult
        }
        return topRated_moviesData

def langs():
    target_langs = ['en', 'ja', 'hi', 'ko', 'it', 'pt', 'es', 'zh', 'fr', 'tr', 'ru']
    
    langURL = f"https://api.themoviedb.org/3/configuration/languages?api_key={TMDB_API_KEY}"
    langs = requests.get(url=langURL)
    langs_data = langs.json()
    
    # Create dictionary with iso_639_1 as keys and full language info as values
    return {
        lang['iso_639_1']: lang 
        for lang in langs_data 
        if lang['iso_639_1'] in target_langs
    }

def film_actor2():
    topRated_moviesID = []
    for i in range(1,6):
        top_ratedURL = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&page={i}&language=en-US"
        topRated = requests.get(url=top_ratedURL)
        topRated_data = topRated.json()
        results = topRated_data.get("results")
        for movie in results:
            film_id = movie["id"]
            topRated_moviesID.append(film_id)

    film_actor = {}
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
        character = main_actor['character']
        actor[main_actor_id]={
            "first_name" : first_name,
            "last_name" : last_name
        }
        film_actor[main_actor_id] = {
            "film_id": movie_id,
            "character": main_actor['character']
        }
        return film_actor,actor
    
def genres():
    genres_id = [35, 18, 80, 12, 16, 28, 37, 14, 27, 53, 10752, 10751, 10749, 10402]
    
    genrsURL = f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={TMDB_API_KEY}"
    genrs = requests.get(url=genrsURL)
    genrs_data = genrs.json()
    
    # Return as dictionary {id: name}
    return {genre['id']: genre['name'] for genre in genrs_data['genres'] if genre['id'] in genres_id}

def filmGenre():
    topRated_moviesID = []
    for i in range(1,6):
        top_ratedURL = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&page={i}&language=en-US"
        topRated = requests.get(url=top_ratedURL)
        topRated_data = topRated.json()
        results = topRated_data.get("results")
        for movie in results:
            film_id = movie["id"]
            topRated_moviesID.append(film_id)

    film_category = {}
    for movie_id in topRated_moviesID:
        movie_detailsURL = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        
        movie_details = requests.get(url=movie_detailsURL)
        movie_details_data = movie_details.json()

        film_id = movie_id
        genre = movie_details_data["genres"][0]["id"]
        film_category[film_id] = {
            "category_id":genre }
        return film_category