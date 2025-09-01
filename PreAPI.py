import os
import requests
from dotenv import load_dotenv
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# STEP 1: Get the top 10 most popular providers in the US
base_link_providers = f"https://api.themoviedb.org/3/watch/providers/movie?api_key={TMDB_API_KEY}&language=en-US&watch_region=US"
providers_response = requests.get(url=base_link_providers)
providers_data = providers_response.json()

# Create dictionary of top 10 providers
top_providers_dict = {}
top_n = 10

sorted_providers = sorted(
    providers_data['results'],
    key=lambda x: x['display_priority']
)[:top_n]

for provider in sorted_providers:
    provider_id = provider['provider_id']
    top_providers_dict[provider_id] = {
        'provider_name': provider['provider_name'],
        'display_priority': provider['display_priority']
    }

print("Top 10 Most Popular Providers in US:")
print(top_providers_dict)

# STEP 2: Check which of these top 10 providers have the movie
base_link_movie = f"https://api.themoviedb.org/3/movie/278/watch/providers?api_key={TMDB_API_KEY}&language=en-US&watch_region=US"
movie_response = requests.get(url=base_link_movie)
movie_data = movie_response.json()
us_providers = movie_data['results'].get('US', {})

print(f"\nChecking which top 10 providers have 'The Shawshank Redemption':")

# Check each category (flatrate, rent, buy) for top providers
available_on = {}

for category in ['flatrate', 'rent', 'buy']:
    if category in us_providers:
        for provider in us_providers[category]:
            if provider['provider_id'] in top_providers_dict:
                provider_id = provider['provider_id']
                if provider_id not in available_on:
                    available_on[provider_id] = {
                        'provider_name': top_providers_dict[provider_id]['provider_name'],
                        'available_for': [category],
                        'display_priority': top_providers_dict[provider_id]['display_priority']
                    }
                else:
                    available_on[provider_id]['available_for'].append(category)

# Sort by display priority (most popular first)
available_on_sorted = dict(sorted(
    available_on.items(),
    key=lambda x: x[1]['display_priority']
))

print("\nTop providers that have the movie:")
for provider_id, info in available_on_sorted.items():
    print(f"{info['provider_name']} (Priority: {info['display_priority']}): Available for {', '.join(info['available_for'])}")