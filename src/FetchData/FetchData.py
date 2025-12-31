from src.FetchData.configuration import TMDB_API_KEY
from src.FetchData.Fetchers.films import topRated_movies
from src.FetchData.Fetchers.langs import langs
from src.FetchData.Fetchers.film_actor import film_actor
from src.FetchData.Fetchers.film_category import film_category
from src.FetchData.Fetchers.inventory_providers import inventory_providers
from src.FetchData.Fetchers.categories import categories
from src.FetchData.Fetchers.customers import fetch_users

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
        countries, cities, addresses, customers = fetch_users()
        return {
            "films": films_data,
            "actors": actors,
            "film_actors": film_actors,
            "film_categories": film_categories,
            "inventory": inventory,
            "providers": providers,
            "categories": categories_data,
            "languages": language_data,
            "countries": countries,
            "cities": cities,
            "addresses": addresses,
            "customers": customers
        }
