#! /usr/bin/python3

import re
from pprint import pprint

def prepare_spotify_search(track_list):
    '''
    searchQueryObjects = [re.sub(r'[,&()]*(ft\.)?(- )?', '', track)
                        for track in track_list]
    pprint(searchQueryObjects) 
 '''
    return track_list