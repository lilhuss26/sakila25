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
