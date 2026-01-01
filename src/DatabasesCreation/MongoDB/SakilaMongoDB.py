from src.DatabasesCreation.MongoDB.configuration import fetcher, sakila25_db
from src.DatabasesCreation.MongoDB.insertion import (insert_films, 
                                                      insert_providers_with_inventory,
                                                      insert_customers_with_all_data)


class SakilaMongoDB:
    def __init__(self):
        self.all_data = fetcher.fetch_all()
        self.db = sakila25_db

    def create(self):
        films = self.all_data["films"]
        actors = self.all_data["actors"]
        film_actors = self.all_data["film_actors"]
        film_categories = self.all_data["film_categories"]
        inventory = self.all_data["inventory"]
        providers = self.all_data["providers"]
        categories = self.all_data["categories"]
        languages = self.all_data["languages"]
        countries = self.all_data["countries"]
        cities = self.all_data["cities"]
        addresses = self.all_data["addresses"]
        customers = self.all_data["customers"]
        cards_data = self.all_data["cards"]

        inventory_with_ids = []
        for i, inv in enumerate(inventory, 1):
            inv_copy = inv.copy()
            inv_copy['inventory_id'] = i
            inventory_with_ids.append(inv_copy)

        insert_films(films, actors, film_actors, film_categories, categories, languages, self.db)
        
        insert_providers_with_inventory(providers, inventory_with_ids, self.db)
        
        insert_customers_with_all_data(countries, cities, addresses, customers, 
                                       cards_data, providers, inventory_with_ids, self.db)
        
        print("MongoDB database created successfully with denormalized structure")
        return True
