# -*- coding: utf-8 -*-

import spotipy
import sys
import os
import json
import pprint

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

# Main definition - constants
menu_actions  = {}

def main_menu():
    os.system('clear')
    
    print "Welcome,\n"
    print "Please choose the menu you want to start:"
    print "1. Track"
    print "2. Artist"
    print "3. Album"
    print "4. User"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    print choice
    exec_menu(choice, '0')
 
    return


# TRACK MENU
def track_menu():
    print "TRACK MENU\n"
    print "1. General Info"
    print "2. Audio Features"
    print "3. Audio Analysis"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice, '1')
    return


def track_info():
	os.system('clear')
	track = raw_input(" >> Track name: ")
	results = spotify.search(q=track, limit=1)
	pprint.pprint(results)
	press_to_go_back(1)


def track_features():
	os.system('clear')
	track = raw_input(" >> Track name: ")
	results = spotify.search(q=track, limit=1)
	track_id = results['tracks']['items'][0]['id']
	pprint.pprint(spotify.audio_features([track_id]))
	press_to_go_back(1)


def track_analysis():
	os.system('clear')
	track = raw_input(" >> Track name: ")
	results = spotify.search(q=track, limit=1)
	track_id = results['tracks']['items'][0]['id']
	pprint.pprint(spotify.audio_analysis(track_id))
	press_to_go_back(1)
 

# ARTIST MENU
def artist_menu():
    print "ARTIST MENU\n"
    print "1. General Info"
    print "2. Albums"
    print "3. Top Tracks"
    print "4. Related Artists"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice, '2')
    return


def artist_info():
	os.system('clear')
	artist = raw_input(" >> Artist name: ")
	results = spotify.search(q=artist, limit=1, type='artist')
	pprint.pprint(results)
	press_to_go_back(2)


def artist_albums():
	os.system('clear')
	artist = raw_input(" >> Artist name: ")
	results = spotify.search(q=artist, limit=1, type='artist')
	artist_id = results['artists']['items'][0]['id']
	pprint.pprint(spotify.artist_albums(artist_id, album_type='album'))
	press_to_go_back(2)


def artist_top_tracks():
	os.system('clear')
	artist = raw_input(" >> Artist name: ")
	results = spotify.search(q=artist, limit=1, type='artist')
	artist_id = results['artists']['items'][0]['id']
	pprint.pprint(spotify.artist_top_tracks(artist_id, country='PT'))
	press_to_go_back(2)


def artist_related_artists():
	os.system('clear')
	artist = raw_input(" >> Artist name: ")
	results = spotify.search(q=artist, limit=1, type='artist')
	artist_id = results['artists']['items'][0]['id']
	pprint.pprint(spotify.artist_related_artists(artist_id))
	press_to_go_back(2)


# ALBUM MENU
def album_menu():
    print "ALBUM MENU\n"
    print "1. General Info"
    print "2. Album Tracks"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice, '3')
    return


def album_info():
	os.system('clear')
	album = raw_input(" >> Album name: ")
	results = spotify.search(q=album, limit=1, type='album')
	pprint.pprint(results)
	press_to_go_back(3)


def album_tracks():
	os.system('clear')
	album = raw_input(" >> Album name: ")
	results = spotify.search(q=album, limit=1, type='album')
	album_id = results['albums']['items'][0]['id']
	pprint.pprint(spotify.album_tracks(album_id))
	press_to_go_back(3)


# USER MENU
def user_menu():
    print "USER MENU\n"
    print "1. Top Tracks"
    print "2. Top Artists"
    print "3. Recently Played Tracks"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice, '4')
    return


def user_top_tracks():
	os.system('clear')
	username = raw_input(" >> Username: ")
	scope = 'user-top-read'
	token = util.prompt_for_user_token(username, scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)
	spotify = spotipy.Spotify(auth=token)
	results = spotify.current_user_top_tracks()
	pprint.pprint(results)
	press_to_go_back(4)


def user_top_artists():
	os.system('clear')
	username = raw_input(" >> Username: ")
	scope = 'user-top-read'
	token = util.prompt_for_user_token(username, scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)
	spotify = spotipy.Spotify(auth=token)
	results = spotify.current_user_top_artists()
	pprint.pprint(results)
	press_to_go_back(4)


def user_recent_tracks():
	os.system('clear')
	username = raw_input(" >> Username: ")
	scope = 'user-read-recently-played'
	token = util.prompt_for_user_token(username, scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)
	spotify = spotipy.Spotify(auth=token)
	results = spotify.current_user_recently_played()
	pprint.pprint(results)
	press_to_go_back(4)


def exec_menu(choice, menu_id):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[menu_id][ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions[menu_id]['menu']()
    return


def press_to_go_back(menu_id):
	raw_input(">> Press to go back to menu")
	os.system('clear')
	menu_actions[str(menu_id)]['menu']()


# Back to main menu
def back():
    menu_actions['0']['menu']()

 
# Exit program
def exit():
    sys.exit()


# Menu definition
menu_actions = {
	'0' : {
		'menu': main_menu,
		'1': track_menu,
		'2': artist_menu,
		'3': album_menu,
		'4': user_menu,
		'9': back,
		'0': exit,
	},
	'1' : {
		'menu': track_menu,
		'1': track_info,
		'2': track_features,
		'3': track_analysis,
		'9': back,
		'0': exit,
	},
	'2' : {
		'menu': artist_menu,
		'1': artist_info,
		'2': artist_albums,
		'3': artist_top_tracks,
		'4': artist_related_artists,
		'9': back,
		'0': exit,
	},
	'3' : {
		'menu': album_menu,
		'1': album_info,
		'2': album_tracks,
		'9': back,
		'0': exit,
	},
	'4' : {
		'menu': user_menu,
		'1': user_top_tracks,
		'2': user_top_artists,
		'3': user_recent_tracks,
		'9': back,
		'0': exit,
	},
}


if __name__ == '__main__':
	main_menu()