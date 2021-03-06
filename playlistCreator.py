# This script logs in to spotify and creates a specific playlist so far - TODO: extend this

import pprint
import sys
import spotipy
import spotipy.util as util
from json_sorter import bestFit

client_id = 'd02535ac05c14639beceb6d302177372'
client_secret = '87b07a1e938f4a76a2c2affe86a47e22'
redirect_uri = 'http://localhost:8080'
master_user = "11171394439"
sp = spotipy.Spotify();


scope = 'playlist-modify-public'
token = util.prompt_for_user_token(master_user, scope, client_id, client_secret, redirect_uri)
if token:
	    sp = spotipy.Spotify(auth=token)
else:
	    print ("Can't get token for", master_user)


def createPlaylist(username, moods, n):

	track_ids = bestFit(moods, n)
	playlist_attr = sp.user_playlist_create(username, "Your current mood", True);
	playlist_id = playlist_attr ['id']
	sp.user_playlist_add_tracks(username, playlist_id, track_ids)
	return playlist_id;

def generateLink(moods):
	playlist_id = createPlaylist(master_user, moods, 20)
	return "https://open.spotify.com/playlist/" + playlist_id;