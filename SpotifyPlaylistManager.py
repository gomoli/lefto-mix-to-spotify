import time
from pprint import pprint
import spotipy

spotify = spotipy.Spotify()

def search_track(track):
    print('Looking up:\t %s' % track)
    time.sleep(1)
    results = spotify.search(track, limit=10, offset=0, type='track')
    if results['tracks']['items']:
        print("Found:\t\t " + results['tracks']['items'][0]['name'])
        return results['tracks']['items'][0]['id']
    else:
        print('\tNo results found')
        return

def add_to_playlist(track, playlist):
    return
