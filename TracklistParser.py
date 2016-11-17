#! /usr/bin/python3

import re
from pprint import pprint

def prepareSpotifySearch(trackList):
    searchQueryObjects = [re.sub(r'[,&()]*(ft\.)?(- )?', '', track)
                        for track in trackList]
    pprint(searchQueryObjects)
    return searchQueryObjects