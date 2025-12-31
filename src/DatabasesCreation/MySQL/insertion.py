from src.DatabasesCreation.MySQL.configuration import sakila25_engine
from sqlalchemy.orm import Session
session = Session(sakila25_engine)
from src.DatabasesCreation.MySQL.schema import Language,Film,Category,FilmCategory,Actor,FilmActor, Provider, Inventory, Country, City, Address, Customer
import random

def mysql_insert_langs(language_data):
    for iso_code, lang_info in language_data.items():
        lang_info['language_iso_639_1'] = iso_code
        session.merge(Language(**lang_info))
    session.commit()
    print("Languages inserted successfully")

def mysql_insert_film(film_data):
    for film_id, film_info in film_data.items():
        film_info['film_id'] = film_id
        session.merge(Film(**film_info))
    session.commit()
    print("Films inserted successfully")

def mysql_insert_category(category_data):
    for category_id, category_info in category_data.items():
        category_info['category_id'] = category_id
        session.merge(Category(**category_info))
    session.commit()
    print("Categories inserted successfully")

def mysql_insert_actor(actor_data):
    for actor_id, actor_info in actor_data.items():
        actor_info['actor_id'] = actor_id
        session.merge(Actor(**actor_info))
    session.commit()
    print("Actors inserted successfully")

def mysql_insert_film_actor(film_actor_data):
    for film_actor in film_actor_data:
        session.merge(FilmActor(**film_actor))
    session.commit()
    print("Film actors inserted successfully")

def mysql_insert_film_category(film_category_data):
    for film_id, film_category_info in film_category_data.items():
        session.merge(FilmCategory(film_id=film_id,
                                   category_id=film_category_info["category_id"]))

    session.commit()
    print("Film categories inserted successfully")

def mysql_insert_provider(provider_data):
    for provider_id, provider_info in provider_data.items():
        provider_info['provider_id'] = provider_id
        session.merge(Provider(**provider_info))
    session.commit()
    print("Providers inserted successfully")

def mysql_insert_inventory(inventory_data):
    for inventory_info in inventory_data:
        session.merge(Inventory(**inventory_info))
    session.commit()
    print("Inventory inserted successfully")

def mysql_insert_users_data(countries_data, cities_data, addresses_data, customers_data):
    country_map = {}
    for country_name, country_code in countries_data.items():
        country = Country(country=country_name, country_slag=country_code)
        session.add(country)
        session.flush()
        country_map[country_name] = country.country_id
    
    city_map = {}
    for city_name, country_name in cities_data:
        city = City(city=city_name, country_id=country_map[country_name])
        session.add(city)
        session.flush()
        city_map[(city_name, country_name)] = city.city_id
        
    address_map = {}
    for addr in addresses_data:
        city_id = city_map[(addr['city'], addr['country'])]
        address_obj = Address(
            address=addr['address'],
            address2=None,
            state=addr['state'],
            postal_code=addr['postal_code'],
            offset=addr['offset'],
            city_id=city_id
        )
        session.add(address_obj)
        session.flush()
        address_map[(addr['address'], addr['postal_code'])] = address_obj.address_id

    providers = session.query(Provider.provider_id).all()
    provider_ids = [p.provider_id for p in providers]

    for cust in customers_data:
        address_id = address_map[(cust['address'], cust['postal_code'])]
        customer = Customer(
            customer_id=cust['customer_id'],
            first_name=cust['first_name'],
            last_name=cust['last_name'],
            email=cust['email'],
            address_id=address_id,
            active=True,
            create_date=cust['create_date'],
            provider_id=random.choice(provider_ids) if provider_ids else None,
            date_of_birth=cust['date_of_birth']
        )
        session.add(customer)
    
    session.commit()
    print("Users data (Countries, Cities, Addresses, Customers) inserted successfully") 