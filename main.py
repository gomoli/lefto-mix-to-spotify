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
    track_list = spider.run('fresh')
    track_list = prepare_spotify_search(track_list)
    for track in track_list:
        track_id = search_track(track)
        if track_id:
            print("\t" + track_id)
elif options.archive:
    mixes = spider.run('archive')
    for mix in mixes:
        track_list = prepare_spotify_search(mix)
        for track in track_list:
            search_track(track)
else:
    print("Please supply a -f or -a argument.")
    quit()
