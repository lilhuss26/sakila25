import os
import requests
from dotenv import load_dotenv
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

base_link = f"https://api.themoviedb.org/3/watch/providers/movie?api_key={TMDB_API_KEY}&language=en-US&watch_region=US"
providers = requests.get(url=base_link)
providers_data = providers.json()


popular_providers_dict = {}
top_n = 10  

sorted_providers = sorted(
    providers_data['results'],
    key=lambda x: x['display_priority']
)[:top_n]

for provider in sorted_providers:
    provider_id = provider['provider_id']
    popular_providers_dict[provider_id] = {
        'provider_name': provider['provider_name'],
        'display_priority': provider['display_priority']
    }

print("Most Popular Providers Dictionary:")
print(popular_providers_dict)

print("\nAccessing Netflix (ID: 8):")
print(popular_providers_dict[8])