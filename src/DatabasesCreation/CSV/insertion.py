import pandas as pd

def csv_films(films, dir):
    movie_rate_df = pd.DataFrame.from_dict(films, orient='index')
    movie_rate_df = movie_rate_df.rename_axis('film_id')
    movie_rate_df = movie_rate_df.reset_index()
    movie_rate_df.to_csv(f"{dir}/film.csv", index=False)
    print("films inserted successfully")

def csv_actor(actor, dir):
    actor_df = pd.DataFrame.from_dict(actor, orient='index')
    actor_df = actor_df.rename_axis('actor_id')
    actor_df = actor_df.reset_index()
    actor_df.to_csv(f"{dir}/actor.csv", index=False)
    print("actors inserted successfully")

def csv_film_actor(film_actor, dir):
    film_actor_df = pd.DataFrame(film_actor)
    film_actor_df.to_csv(f"{dir}/film_actor.csv", index=False)
    print("film actors inserted successfully")

def csv_film_category(film_category, dir):
    film_category_df = pd.DataFrame.from_dict(film_category, orient='index')
    film_category_df = film_category_df.rename_axis('film_id')
    film_category_df = film_category_df.reset_index()
    film_category_df.to_csv(f"{dir}/film_category.csv", index=False)
    print("film categories inserted successfully")

def csv_category(categories, dir):
    category_df = pd.DataFrame.from_dict(categories, orient='index', columns=['name'])
    category_df = category_df.rename_axis('category_id')
    category_df = category_df.reset_index()
    category_df.to_csv(f"{dir}/category.csv", index=False)
    print("category inserted successfully")

def csv_inventory(inventory, dir):
    inventory_df = pd.DataFrame(inventory)
    inventory_df.to_csv(f"{dir}/inventory.csv", index=False)
    print("inventory inserted successfully")

def csv_providers(providers, dir):
    providers_df = pd.DataFrame.from_dict(providers, orient='index').reset_index()
    providers_df = providers_df.rename(columns={'index': 'provider_id'})
    providers_df.to_csv(f"{dir}/providers.csv", index=False)
    print("providers inserted successfully")

def csv_language(langs, dir):
    langs_df = pd.DataFrame.from_dict(langs, orient='index')
    langs_df = langs_df.reset_index()
    langs_df.to_csv(f"{dir}/language.csv", index=False)
    print("language inserted successfully")

import random

def csv_users_data(countries, cities, addresses, customers, provider_ids, dir):
    country_list = []
    country_map = {} # name -> id
    for i, (name, code) in enumerate(countries.items(), 1):
        country_list.append({
            'country_id': i,
            'country': name,
            'country_slag': code
        })
        country_map[name] = i
    
    pd.DataFrame(country_list).to_csv(f"{dir}/country.csv", index=False)
    print("countries inserted successfully")

    city_list = []
    city_map = {}
    for i, (city_name, country_name) in enumerate(cities, 1):
        city_list.append({
            'city_id': i,
            'city': city_name,
            'country_id': country_map[country_name]
        })
        city_map[(city_name, country_name)] = i
        
    pd.DataFrame(city_list).to_csv(f"{dir}/city.csv", index=False)
    print("cities inserted successfully")

    address_list = []
    address_map = {}
    for i, addr in enumerate(addresses, 1):
        city_id = city_map[(addr['city'], addr['country'])]
        address_list.append({
            'address_id': i,
            'address': addr['address'],
            'address2': None,
            'state': addr['state'],
            'city_id': city_id,
            'postal_code': addr['postal_code'],
            'offset': addr['offset']
        })
        address_map[(addr['address'], addr['postal_code'])] = i
        
    pd.DataFrame(address_list).to_csv(f"{dir}/address.csv", index=False)
    print("addresses inserted successfully")

    customer_list = []
    for cust in customers:
        address_id = address_map[(cust['address'], cust['postal_code'])]
        customer_list.append({
            'customer_id': cust['customer_id'],
            'first_name': cust['first_name'],
            'last_name': cust['last_name'],
            'email': cust['email'],
            'address_id': address_id,
            'active': True,
            'create_date': cust['create_date'],
            'provider_id': random.choice(provider_ids) if provider_ids else None,
            'date_of_birth': cust['date_of_birth'],
            'gender': cust['gender']
        })
        
    pd.DataFrame(customer_list).to_csv(f"{dir}/customer.csv", index=False)
    print("customers inserted successfully")
