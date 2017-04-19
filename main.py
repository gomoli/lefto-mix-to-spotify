from pprint import pprint
from optparse import OptionParser
from settings import load_env_variables
from MixcloudSpider import LeftoSpider
from TracklistParser import prepare_spotify_search
from SpotifyPlaylistManager import search_track
import spotipy.util as util
import spotipy

parser = OptionParser()
parser.add_option("-f", "--fresh", action="store_true", dest="fresh", default=False)
parser.add_option("-a", "--archive", action="store_true", dest="archive", default=False)
(options, args) = parser.parse_args()

scope = 'playlist-modify-public'
username = 'idberend'
load_env_variables()

token = util.prompt_for_user_token(username, scope)
if token:
    sp = spotipy.Spotify(auth='token')

if __name__ == "__main__":
    spider = LeftoSpider()
    if options.fresh:
        track_list = spider.run('fresh')
        track_list = prepare_spotify_search(track_list)
        if spider.TRACKLIST:
            spotify_list = []
            for track in track_list:
                track_id = search_track(track)
                if track_id:
                    spotify_list.append(track_id)
                    print("\t\t" + track_id)
        else:
            print("Found no tracks")

    elif options.archive:
        mixes = spider.run('archive')
        for mix in mixes:
            track_list = prepare_spotify_search(mix)
            for track in track_list:
                search_track(track)
    else:
        print("Please supply a -f or -a argument.")
        quit()

sp.trace = False
sp.user_playlist_add_tracks(username, '6mzdLe0e8Oew4kfFN6845f', spotify_list)