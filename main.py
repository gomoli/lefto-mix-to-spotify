#! /usr/bin/python3

from pprint import pprint
from optparse import OptionParser
from MixcloudSpider import LeftoSpider
from TracklistParser import prepare_spotify_search
from SpotifyPlaylistManager import search_track

parser = OptionParser()
parser.add_option("-f", "--fresh", action="store_true", dest="fresh", default=False)
parser.add_option("-a", "--archive", action="store_true", dest="archive", default=False)
(options, args) = parser.parse_args()

spider = LeftoSpider()
if options.fresh:
    tracklist = spider.run('fresh')
elif options.archive:
    tracklist = spider.run('archive')

query = prepare_spotify_search(tracklist)
for item in query:
    pprint(search_track(item))
