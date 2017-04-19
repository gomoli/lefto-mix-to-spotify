import re
from pprint import pprint

def prepare_spotify_search(track_list):
    stripped_track_list = [re.sub(r'\.', ' ', track)
                        for track in track_list]
    return stripped_track_list