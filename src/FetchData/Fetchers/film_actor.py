import requests
from ..utils import top_rated_movies_ids
def film_actor(key: str, pages : int = 6):
    topRated_moviesID = top_rated_movies_ids(key=key, pages=pages)

    film_actor = []
    actor = {}
    for movie_id in topRated_moviesID:
        creditsURL = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={key}&language=en-US"
        credits = requests.get(url=creditsURL)
        credits_data = credits.json()
        # film_id = movie_id
        main_actor = credits_data['cast'][0]
        main_actor_id = main_actor['id']
        main_actor_name = main_actor['name']
        name_parts = main_actor_name.split()
        first_name = name_parts[0] if len(name_parts) > 0 else ""
        last_name = name_parts[1] if len(name_parts) > 1 else ""
        character = main_actor['character']
        actor[main_actor_id] = {
            "first_name": first_name,
            "last_name": last_name
        }
        film_actor.append({
            "actor_id": main_actor_id,
            "film_id": movie_id,
            "character": character
        })

    return actor, film_actor
