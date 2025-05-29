import pandas as pd 
df = pd.read_csv('top_rated_movies.csv')
print(df['language'].unique())