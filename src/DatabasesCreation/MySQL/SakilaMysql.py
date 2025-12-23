from configuration import fetcher
from Insertion import *

class SakilaMysql:
    def __init__(self):
        self.all_data = fetcher.fetch_all()

    def create(self):
        films = self.all_data["films"]
        actor = self.all_data["actors"]
        film_actor = self.all_data["film_actors"]
        film_category = self.all_data["film_categories"]
        inventory = self.all_data["inventory"]
        providers = self.all_data["providers"]
        categories =self.all_data["categories"]
        language = self.all_data["languages"]

        mysql_insert_film(film_data=films)
        mysql_insert_actor(actor_data=actor, film_actor_data=film_actor)
        mysql_insert_film_category(film_category_data=film_category)
        mysql_insert_category(category_data=categories)
        mysql_insert_langs(language_data=language)
        return True