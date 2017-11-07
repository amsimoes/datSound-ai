# -*- coding: utf-8 -*-

import spotipy
import sys
import time
import json

import spotipy.oauth2 as oauth2
import spotipy.util as util

CLIENT_ID = '7cc49bc4930c43f28ce2bc3740afb797'
CLIENT_SECRET = '9c1de0f1c11d41078d0778a9242769d9'
REDIRECT_URI='http://localhost/'

'''
	Musica (query) -> Features / Analysis / Genre
	Artista (query) -> Top Tracks / Top Albuns / Related Artists
	User -> Top Tracks / Top Artists / Events near? / Followers?

	Authorization Code Flow -> private / longer
	Clients Credentials -> Appropriate for requests that do not require access to a user’s private data. 

'''

credentials = oauth2.SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

username = 'megustatumadre'

if token:
    playlists = spotify.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'])
else:
    print("Can't get token for", username)
