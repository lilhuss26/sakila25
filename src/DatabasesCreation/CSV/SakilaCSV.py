from configuration import DIR, fetcher
from Insertion import *

class SakilaCSV:
    def __init__(self):
        self.all_data = fetcher.fetch_all()
        self.dir = DIR
    def create(self):
        films = self.all_data["films"]
        actor = self.all_data["actors"]
        film_actor = self.all_data["film_actors"]
        film_category = self.all_data["film_categories"]
        inventory = self.all_data["inventory"]
        providers = self.all_data["providers"]
        categories =self.all_data["categories"]
        language = self.all_data["languages"]

        csv_films(films, self.dir)
        csv_actor(actor, self.dir)
        csv_film_actor(film_actor, self.dir)
        csv_film_category(film_category, self.dir)
        csv_category(categories, self.dir)
        csv_inventory(inventory, self.dir)
        csv_providers(providers, self.dir)
        csv_language(language, self.dir)
        return True