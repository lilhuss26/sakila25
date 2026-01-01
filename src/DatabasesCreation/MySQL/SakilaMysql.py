from src.DatabasesCreation.MySQL.configuration import fetcher
from src.DatabasesCreation.MySQL.insertion import *

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
        countries = self.all_data["countries"]
        cities = self.all_data["cities"]
        addresses = self.all_data["addresses"]
        customers = self.all_data["customers"]
        cards_data = self.all_data["cards"]

        mysql_insert_langs(language_data=language)
        mysql_insert_category(category_data=categories)
        mysql_insert_actor(actor_data=actor)
        mysql_insert_provider(provider_data=providers)
        mysql_insert_film(film_data=films)

        mysql_insert_inventory(inventory_data=inventory)
        mysql_insert_film_category(film_category_data=film_category)
        mysql_insert_film_actor(film_actor_data=film_actor)

        mysql_insert_users_data(countries_data=countries,
                              cities_data=cities,
                              addresses_data=addresses,
                              customers_data=customers)
        
        mysql_insert_cards(cards_data=cards_data)
        
        mysql_insert_subscriptions()
        mysql_insert_payments()
        return True