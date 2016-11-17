#! /usr/bin/python3

import spotipy
from pprint import pprint

spotify = spotipy.Spotify()

def searchTrack(query):
    results = spotify.search(query)
    for track in results['tracks']['items']:
        pprint(track['name'])
        return track['id']