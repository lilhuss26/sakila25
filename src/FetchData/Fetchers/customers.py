import requests
from datetime import datetime

def fetch_users(quantity: int = 100):
    base_url = f"https://randomuser.me/api/?results={quantity}&nat=us,au,br,ca,fr,gb"
    response = requests.get(base_url)
    users_data = response.json()['results']
    
    countries = {}
    cities = set()
    addresses = []
    customers = []
    
    for user in users_data:
        country_name = user['location']['country']
        country_code = user['nat']
        city_name = user['location']['city']
        street = user['location']['street']
        
        countries[country_name] = country_code
        cities.add((city_name, country_name))
        
        address_str = f"{street['number']} {street['name']}"
        addresses.append({
            'address': address_str,
            'state': user['location']['state'],
            'postal_code': str(user['location']['postcode']),
            'offset': user['location']['timezone']['offset'],
            'city': city_name,
            'country': country_name
        })
        
        customers.append({
            'customer_id': user['login']['uuid'],
            'first_name': user['name']['first'],
            'last_name': user['name']['last'],
            'email': user['email'],
            'create_date': datetime.fromisoformat(user['registered']['date'].replace('Z', '+00:00')),
            'date_of_birth': datetime.fromisoformat(user['dob']['date'].replace('Z', '+00:00')),
            'address': address_str,
            'postal_code': str(user['location']['postcode']),
            'gender': user['gender']
        })
    
    print("users_data fetched successfully")
    return countries, cities, addresses, customers
