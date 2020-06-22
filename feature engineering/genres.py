from imdb import IMDb
import pandas as pd
import numpy as np
import csv
import json

ia = IMDb()

file = open('/Users/nick/Desktop/PythonData/tmdb-box-office-prediction/train.csv')
data = pd.read_csv('/Users/nick/Desktop/PythonData/tmdb-box-office-prediction/train.csv')

#Full set
df = pd.DataFrame(data=data)
# print(df)

movie = ia.get_movie(df['imdb_id'][2][2:])

# Removing irrelevant fields
df_1 = df.drop(columns=['belongs_to_collection', 'homepage', 'poster_path', 'original_title', 'overview','tagline','Keywords', 'popularity'])
# print(df_1)

# Featurizing Columns - genres
df_2 = pd.Series([(['Comedy']), ('Comedy', 'Drama', 'Family', 'Romance'), (['Drama']), ('Thriller', 'Drama'), ('Action', 'Thriller'), ('Animation', 'Adventure', 'Family')]).apply(frozenset).to_frame(name='genre')
for genre in frozenset.union(*df_2.genre):
    df_2[genre] = df_2.apply(lambda _: int(genre in _.genre), axis=1)
print(df_2)

#Encoding JSON Data