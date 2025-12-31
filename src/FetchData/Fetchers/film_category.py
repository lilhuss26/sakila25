import requests
from ..utils import top_rated_movies_ids
def film_category(key: str, pages : int = 6):
    topRated_moviesID = top_rated_movies_ids(key=key, pages=pages)

    film_category = {}
    for movie_id in topRated_moviesID:
        movie_detailsURL = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={key}&language=en-US"

        movie_details = requests.get(url=movie_detailsURL)
        movie_details_data = movie_details.json()

        film_id = movie_id
        genre = movie_details_data["genres"][0]["id"]
        film_category[film_id] = {
            "category_id": genre}
    print("film_category fetched successfully")
    return film_category