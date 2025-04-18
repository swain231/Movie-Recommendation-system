import pandas as pd
import random

class MovieRecommender:
    def __init__(self, file_path='data/movies.csv'):
        self.movies = pd.read_csv(file_path)

    def recommend_by_genre(self, genre):
        matches = self.movies[self.movies['genre'].str.contains(genre, case=False)]
        if matches.empty:
            return []
        return random.sample(matches['title'].tolist(), min(3, len(matches)))
