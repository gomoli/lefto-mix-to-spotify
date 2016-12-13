import time
from pprint import pprint
import spotipy

spotify = spotipy.Spotify()

def search_track(track):
    print('Looking up: %s' % track)
    time.sleep(1)
    results = spotify.search(track, limit=10, offset=0, type='track')
    if results['tracks']['items']:
        print("\t" + results['tracks']['items'][0]['name'])
        return results['tracks']['items'][0]['id']
    else:
        print('No results found')
        return
