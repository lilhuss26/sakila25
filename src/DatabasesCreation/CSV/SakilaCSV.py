from src.DatabasesCreation.CSV.configuration import DIR, fetcher
from src.DatabasesCreation.CSV.insertion import *

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
        countries = self.all_data["countries"]
        cities = self.all_data["cities"]
        addresses = self.all_data["addresses"]
        customers = self.all_data["customers"]
        cards_data = self.all_data["cards"]
        provider_ids = list(providers.keys())

        csv_films(films, self.dir)
        csv_actor(actor, self.dir)
        csv_film_actor(film_actor, self.dir)
        csv_film_category(film_category, self.dir)
        csv_category(categories, self.dir)
        inventory_list = csv_inventory(inventory, self.dir)
        csv_providers(providers, self.dir)
        csv_language(language, self.dir)
        csv_users_data(countries, cities, addresses, customers, provider_ids, self.dir)
        
        customer_card_map = csv_cards(cards_data, customers, self.dir)
        subscriptions_list = csv_subscriptions(customers, inventory_list, providers, self.dir)
        csv_payments(subscriptions_list, customer_card_map, self.dir)
        
        return True