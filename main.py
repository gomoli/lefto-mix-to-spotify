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
    pprint(search_track([track for track in tracklist]))
elif options.archive:
    mixes = spider.run('archive')
    for mix in mixes:
        pprint(search_track([track for track in mix]))

