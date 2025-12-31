import requests
from ..utils import top_rated_movies_ids
def inventory_providers(key: str, pages: int = 6):
    topRated_moviesID = top_rated_movies_ids(key=key, pages=pages)

    inventory_records = []
    providers = {}
    country_code = "US"

    for movie_id in topRated_moviesID:
        movie_providersURL = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={key}&language=en-US"
        movie_providers = requests.get(url=movie_providersURL)
        movie_providers_data = movie_providers.json()

        country_data = movie_providers_data.get("results", {}).get(country_code)
        if not country_data:
            continue

        unique_providers_for_movie = set()

        for provider_type in ["flatrate", "rent", "buy"]:
            providers_list = country_data.get(provider_type, [])
            if providers_list:
                    first_provider = providers_list[0]
                    provider_id = first_provider["provider_id"]
                    provider_name = first_provider["provider_name"]

                    if provider_id not in unique_providers_for_movie:
                        unique_providers_for_movie.add(provider_id)
                        inventory_records.append({
                            "film_id": movie_id,
                            "provider_id": provider_id
                        })

                    if provider_id not in providers:
                        providers[provider_id] = {
                            "provider_name": provider_name,
                            "country": country_code,
                            "type": provider_type
                        }
    print("inventory_providers fetched successfully")
    return inventory_records, providers