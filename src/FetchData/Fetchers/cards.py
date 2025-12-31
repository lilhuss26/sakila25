import requests

def cards(quantity: int = 100):
    cards_data = requests.get(f"https://fakerapi.it/api/v2/creditCards?_quantity={quantity}")
    cards_data = cards_data.json()
    return cards_data
