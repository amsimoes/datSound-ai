# -*- coding: utf-8 -*-

import spotipy
import sys
import os
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
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice, '1')
    return
 

def artist_menu():
    print "ARTIST MENU\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice, '2')
    return


def album_menu():
    print "ALBUM MENU\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice, '3')
    return


def user_menu():
    print "USER MENU\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice, '4')
    return


def exec_menu(choice, menu_id):
    print choice
    os.system('clear')
    ch = choice.lower()
    print ch
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[menu_id][ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions[menu_id]['menu']()
    return


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
		'9': back,
		'0': exit,
	},
	'2' : {
		'menu': artist_menu,
		'9': back,
		'0': exit,
	},
	'3' : {
		'menu': album_menu,
		'9': back,
		'0': exit,
	},
	'4' : {
		'menu': user_menu,
		'9': back,
		'0': exit,
	},
}


if __name__ == '__main__':
	main_menu()