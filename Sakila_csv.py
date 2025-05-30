from GetAPI import *
import pandas as pd

topRated_moviesData = topRated_movies()
filtered_langs = langs()
actor,film_actor = film_actor2()
filtered_genrs = genres()
film_category = filmGenre()

movie_rate_df = pd.DataFrame.from_dict(topRated_moviesData, orient='index')
movie_rate_df = movie_rate_df.rename_axis('film_id')
movie_rate_df = movie_rate_df.reset_index()
movie_rate_df.to_csv("Sakila_csv/top_rated_movies.csv", index=False)

langs_df = pd.DataFrame.from_dict(filtered_langs)
langs_df.to_csv("Sakila_csv/langs.csv", index=False)

actor_df = pd.DataFrame.from_dict(actor, orient='index')
actor_df = actor_df.rename_axis('actoe_id')
actor_df = actor_df.reset_index()
actor_df.to_csv("Sakila_csv/actor.csv", index=False)

film_actor_df = pd.DataFrame.from_dict(film_actor)
film_actor_df.to_csv("Sakila_csv/film_actor.csv", index=False)

df = pd.DataFrame.from_dict(filtered_genrs)
df.to_csv("Sakila_csv/category.csv", index=False)

movie_rate_df = pd.DataFrame.from_dict(film_category, orient='index')
movie_rate_df = movie_rate_df.rename_axis('film_id')
movie_rate_df = movie_rate_df.reset_index()
movie_rate_df.to_csv("Sakila_csv/film_category.csv", index=False)

