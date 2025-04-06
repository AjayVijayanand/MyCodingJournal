import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd``

data = pd.read_csv('/Users/ajvj56/MyCSJournalAJVJ/test.py', encoding='ISO-8859-1')

feature_names = ["danceability_%", "valence_%", "energy_%", "acousticness_%", "instrumentalness_%", "liveness_%", "speechiness_%"]

X, y = data[feature_names], data['popularity']
