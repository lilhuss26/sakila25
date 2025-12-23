from configuration import TMDB_API_KEY
from Fetchers.films import topRated_movies
from Fetchers.langs import langs
from Fetchers.film_actor import film_actor
from Fetchers.film_category import film_category
from Fetchers.inventory_providers import inventory_providers
from Fetchers.categories import categories
class FetchData:
    def __init__(self, pages: int = 6):
        self.api_key = TMDB_API_KEY
        self.pages = pages

    def fetch_all(self):
        films_data = topRated_movies(key=self.api_key)
        actors, film_actors = film_actor(key=self.api_key, pages=self.pages)
        film_categories = film_category(key=self.api_key, pages=self.pages)
        inventory, providers = inventory_providers(key=self.api_key, pages=self.pages)
        categories_data = categories(key=self.api_key)
        language_data = langs(key=self.api_key)
        return {
            "films": films_data,
            "actors": actors,
            "film_actors": film_actors,
            "film_categories": film_categories,
            "inventory": inventory,
            "providers": providers,
            "categories": categories_data,
            "languages": language_data
        }
