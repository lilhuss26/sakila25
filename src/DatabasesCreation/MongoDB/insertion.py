import random
from datetime import datetime, timedelta

def insert_films(films_data, actors_data, film_actors_data, film_categories_data, categories_data, languages_data, db):
    film_actor_map = {}
    for fa in film_actors_data:
        film_id = fa['film_id']
        if film_id not in film_actor_map:
            film_actor_map[film_id] = []
        actor_info = actors_data.get(fa['actor_id'], {})
        film_actor_map[film_id].append({
            'actor_id': fa['actor_id'],
            'first_name': actor_info.get('first_name'),
            'last_name': actor_info.get('last_name'),
            'character': fa.get('character')
        })
    
    film_category_map = {}
    for film_id, category_ids in film_categories_data.items():
        film_category_map[film_id] = [
            {'category_id': cat_id, 'name': categories_data.get(cat_id, {}).get('name')}
            for cat_id in category_ids
        ]
    
    films_documents = []
    for film in films_data:
        film_id = film['film_id']
        lang_code = film.get('language_iso_639_1')
        language_info = languages_data.get(lang_code, {})
        
        films_documents.append({
            'film_id': film_id,
            'title': film.get('title'),
            'rating': float(film.get('rating', 0)),
            'description': film.get('description'),
            'release_date': film.get('release_date'),
            'popularity': float(film.get('popularity', 0)),
            'revenue': film.get('revenue'),
            'runtime': film.get('runtime'),
            'adult': film.get('adult'),
            'language': {
                'iso_639_1': lang_code,
                'english_name': language_info.get('english_name'),
                'name': language_info.get('name')
            },
            'categories': film_category_map.get(film_id, []),
            'actors': film_actor_map.get(film_id, []),
            'last_update': datetime.now()
        })
    
    db.films.insert_many(films_documents)
    print("Films with embedded actors and categories inserted successfully")

def insert_providers_with_inventory(providers_data, inventory_data, db):
    provider_inventory_map = {}
    for inv in inventory_data:
        provider_id = inv['provider_id']
        if provider_id not in provider_inventory_map:
            provider_inventory_map[provider_id] = []
        provider_inventory_map[provider_id].append({
            'inventory_id': inv.get('inventory_id'),
            'film_id': inv['film_id']
        })
    
    providers_documents = []
    for provider_id, provider_info in providers_data.items():
        providers_documents.append({
            'provider_id': provider_id,
            'provider_name': provider_info.get('provider_name'),
            'type': provider_info.get('type'),
            'country': provider_info.get('country'),
            'inventory': provider_inventory_map.get(provider_id, []),
            'last_update': datetime.now()
        })
    
    db.providers.insert_many(providers_documents)
    print("Providers with embedded inventory inserted successfully")

def insert_customers_with_all_data(countries_data, cities_data, addresses_data, customers_data, 
                                   cards_data, providers_data, inventory_data, db):
    city_map = {}
    for city in cities_data:
        city_id = city['city_id']
        country_info = next((c for c in countries_data if c['country_id'] == city['country_id']), {})
        city_map[city_id] = {
            'city': city.get('city'),
            'country': country_info.get('country'),
            'country_code': country_info.get('country_slag')
        }
    
    address_map = {}
    for addr in addresses_data:
        address_id = addr['address_id']
        city_info = city_map.get(addr['city_id'], {})
        address_map[address_id] = {
            'address': addr.get('address'),
            'address2': addr.get('address2'),
            'state': addr.get('state'),
            'postal_code': addr.get('postal_code'),
            'city': city_info.get('city'),
            'country': city_info.get('country'),
            'country_code': city_info.get('country_code')
        }
    
    customer_card_map = {}
    for i, (customer, card_info) in enumerate(zip(customers_data, cards_data), 1):
        customer_id = customer['customer_id']
        customer_card_map[customer_id] = {
            'card_id': i,
            'card_number': card_info['number'],
            'card_type': card_info['type'],
            'card_expiry_date': card_info['expiration']
        }
    
    provider_inventories = {}
    for inv in inventory_data:
        provider_id = inv['provider_id']
        if provider_id not in provider_inventories:
            provider_inventories[provider_id] = []
        provider_inventories[provider_id].append(inv)
    
    provider_types = {pid: pinfo['type'] for pid, pinfo in providers_data.items()}
    pricing = {'rent': 3.99, 'flatrate': 12.99}
    
    customers_documents = []
    for customer in customers_data:
        customer_id = customer['customer_id']
        address_info = address_map.get(customer['address_id'], {})
        card_info = customer_card_map.get(customer_id, {})
        
        subscriptions = []
        num_subscriptions = random.randint(1, 5)
        available_providers = list(provider_inventories.keys())
        
        if num_subscriptions > len(available_providers):
            num_subscriptions = len(available_providers)
        
        selected_providers = random.sample(available_providers, num_subscriptions)
        
        for idx, provider_id in enumerate(selected_providers, 1):
            inventory_item = random.choice(provider_inventories[provider_id])
            provider_type = provider_types[provider_id]
            
            days_ago = random.randint(0, 365)
            start_date = datetime.now() - timedelta(days=days_ago)
            
            if provider_type == 'rent':
                end_date = start_date + timedelta(days=7)
            else:
                end_date = start_date + timedelta(days=30)
            
            amount = pricing.get(provider_type, 12.99)
            
            subscriptions.append({
                'subscription_id': idx,
                'inventory_id': inventory_item.get('inventory_id'),
                'film_id': inventory_item['film_id'],
                'provider_id': provider_id,
                'provider_name': providers_data[provider_id]['provider_name'],
                'type': provider_type,
                'start_date': start_date,
                'end_date': end_date,
                'payment': {
                    'amount': amount,
                    'payment_date': start_date,
                    'card_id': card_info.get('card_id')
                }
            })
        
        customers_documents.append({
            'customer_id': customer_id,
            'first_name': customer.get('first_name'),
            'last_name': customer.get('last_name'),
            'email': customer.get('email'),
            'active': customer.get('active'),
            'create_date': customer.get('create_date'),
            'date_of_birth': customer.get('date_of_birth'),
            'gender': customer.get('gender'),
            'address': address_info,
            'card': card_info,
            'subscriptions': subscriptions,
            'last_update': datetime.now()
        })
    
    db.customers.insert_many(customers_documents)
    print("Customers with embedded address, card, subscriptions, and payments inserted successfully")
