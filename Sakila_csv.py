from GetAPI import *
import pandas as pd

topRated_moviesData = topRated_movies()
filtered_langs = langs()
actor, film_actor = film_actor2()
filtered_genrs = genres()
film_category = filmGenre()

movie_rate_df = pd.DataFrame.from_dict(topRated_moviesData, orient='index')
movie_rate_df = movie_rate_df.rename_axis('film_id')
movie_rate_df = movie_rate_df.reset_index()
movie_rate_df.to_csv("Sakila_csv/film.csv", index=False)

langs_df = pd.DataFrame.from_dict(filtered_langs, orient='index')
langs_df = langs_df.reset_index()
langs_df.to_csv("Sakila_csv/language.csv", index=False)

actor_df = pd.DataFrame.from_dict(actor, orient='index')
actor_df = actor_df.rename_axis('actor_id')
actor_df = actor_df.reset_index()
actor_df.to_csv("Sakila_csv/actor.csv", index=False)

film_actor_df = pd.DataFrame(film_actor)
film_actor_df.to_csv("Sakila_csv/film_actor.csv", index=False)

category_df = pd.DataFrame.from_dict(filtered_genrs, orient='index', columns=['name'])
category_df = category_df.rename_axis('category_id')
category_df = category_df.reset_index()
category_df.to_csv("Sakila_csv/category.csv", index=False)

film_category_df = pd.DataFrame.from_dict(film_category, orient='index')
film_category_df = film_category_df.rename_axis('film_id')
film_category_df = film_category_df.reset_index()
film_category_df.to_csv("Sakila_csv/film_category.csv", index=False)

inventory, providers = inventory_providers()

inventory_records = []
for movie_id, provider_list in inventory.items():
    for provider in provider_list:
        inventory_records.append({
            "film_id": movie_id,
            "provider_id": provider["provider_id"]
        })

inventory_df = pd.DataFrame(inventory_records)
providers_df = pd.DataFrame.from_dict(providers, orient='index').reset_index()
providers_df = providers_df.rename(columns={'index': 'provider_id'})

inventory_df.to_csv("Sakila_csv/inventory.csv", index=False)
providers_df.to_csv("Sakila_csv/providers.csv", index=False)