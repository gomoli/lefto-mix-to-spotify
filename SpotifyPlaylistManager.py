#! /usr/bin/python3

from pprint import pprint
import spotipy

spotify = spotipy.Spotify()

def search_track(query):
    results = spotify.search(query)
    for track in results['tracks']['items']:
        pprint(track['name'])
        return track['id']
