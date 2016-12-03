#! /usr/bin/python3

import time
from pprint import pprint
import spotipy

spotify = spotipy.Spotify()

def search_track(query):
    time.sleep(2)
    results = spotify.search(query)
    for track in results['tracks']['items']:
        pprint(track['name'])
        return track['id']
