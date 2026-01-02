import random
from datetime import datetime, timedelta

def insert_films(films_data, actors_data, film_actors_data, film_categories_data, categories_data, languages_data, db):
    # Build film-actor mapping
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
    
    # Build film-category mapping
    film_category_map = {}
    for film_id, category_info in film_categories_data.items():
        category_id = category_info.get('category_id')
        if category_id:
            film_category_map[film_id] = [{
                'category_id': category_id,
                'name': categories_data.get(category_id, {}).get('name')
            }]
    
    # Create film documents
    films_documents = []
    for film_id, film_info in films_data.items():
        lang_code = film_info.get('language_iso_639_1')
        language_info = languages_data.get(lang_code, {})
        
        films_documents.append({
            'film_id': film_id,
            'title': film_info.get('title'),
            'rating': float(film_info.get('rating', 0)),
            'description': film_info.get('description'),
            'release_date': film_info.get('release_date'),
            'popularity': float(film_info.get('popularity', 0)),
            'revenue': film_info.get('revenue'),
            'runtime': film_info.get('runtime'),
            'adult': film_info.get('adult'),
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
    # Build address map with embedded city and country info
    address_map = {}
    for i, addr in enumerate(addresses_data):
        city_name = addr.get('city')
        country_name = addr.get('country')
        country_code = countries_data.get(country_name, '')
        
        address_map[i] = {
            'address': addr.get('address'),
            'state': addr.get('state'),
            'postal_code': addr.get('postal_code'),
            'city': city_name,
            'country': country_name,
            'country_code': country_code
        }
    
    # Build customer-card mapping
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
    
    # Create customer documents
    customers_documents = []
    for i, customer in enumerate(customers_data):
        customer_id = customer['customer_id']
        address_info = address_map.get(i, {})
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
