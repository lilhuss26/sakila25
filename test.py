import requests

url = "https://random-data-api.com/api//random_"
response = requests.get(url)
print(response.json())
