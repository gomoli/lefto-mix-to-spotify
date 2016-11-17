#! /usr/bin/python3

from pprint import pprint
from MixcloudSpider import LeftoSpider
from TracklistParser import prepareSpotifySearch
from SpotifyPlaylistManager import searchTrack

spider = LeftoSpider()
tracklist = spider.run('fresh')

query = prepareSpotifySearch(tracklist)
for item in query:
    pprint(searchTrack(item))