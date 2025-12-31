import requests
from ..utils import top_rated_movies_ids
def topRated_movies(key: str, pages: int = 6):
    topRated_moviesID = top_rated_movies_ids(key=key, pages=pages)

    topRated_moviesData = {}
    for movie_id in topRated_moviesID:
        movie_detailsURL = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={key}&language=en-US"

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
            "title": title,
            "rating": rating,
            "description": description,
            "release_date": release_date,
            "language_iso_639_1": language,
            "popularity": popularity,
            "revenue": revenue,
            "runtime": runtime,
            "adult": adult
        }
    print("topRated_movies fetched successfully")
    return topRated_moviesData