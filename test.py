import pandas as pd 
df = pd.read_csv('Sakila_csv/film_category.csv')
print(df['category_id'].unique())