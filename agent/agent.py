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


def recommendations_menu():
    os.system('clear')
    print "RECOMMENDATIONS MENU\n"

    print "1. Based on User's Top Tracks"
    print "2. Based on User's Top Artists"
    print "3. Based on User's Top Tracks and Artists"
    print "4. Based on User's Recently Played Tracks"
    print "5. Based on Users's Top Tracks and Recently Played Tracks"
    print "6. Based on User's Top Genres"
    print "7. Based on User's Top Tracks and Artists and Top Genres"
    print "8. Reset User"
    print "0. Quit\n"

    choice = raw_input(">> ")
    exec_menu(choice, '1')
    return


# doesn't return popularity
def track_features():
    os.system('clear')
    track = raw_input(" >> Track name: ")
    results = spotify.search(q=track, limit=1)
    track_id = results['tracks']['items'][0]['id']
    pprint.pprint(spotify.audio_features([track_id]))
    press_to_go_back(1)


# tuneable track attributes: all got in audio_features
def calc_avg_features(tracks):
    avgs = [['acousticness', 0.0], ['danceability', 0.0], ['duration_ms', 0],
        ['energy', 0.0], ['instrumentalness', 0.0], ['key', 0],
        ['liveness', 0.0], ['loudness', 0.0], ['mode', 0],
        ['speechiness', 0.0], ['tempo', 0.0], ['time_signature', 0],
        ['valence', 0.0]]
    for t_id in tracks:
        results = spotify.audio_features([t_id])
        for at in avgs:
            if type(at[1]) == float:
                at[1] += float(results[0][at[0]])
            else:
                at[1] += int(results[0][at[0]])
    for at in avgs:
        at[1] = at[1] / 5
    return avgs


def generate_array(results, limit):
    arr = []
    for i in range (0, limit):
        arr.append(str(results['items'][i]['id']))
    return arr


def user_top_tracks():
    limit = 5  # maximum = 50
    username = ''
    scope = 'user-top-read'
    token = util.prompt_for_user_token(username, scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)
    spotify = spotipy.Spotify(auth=token)
    results = spotify.current_user_top_tracks()
    # pprint.pprint(results)

    return generate_array(results, limit)


def user_top_artists():
    os.system('clear')
    limit = 5
    username = ''
    scope = 'user-top-read'
    token = util.prompt_for_user_token(username, scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)
    spotify = spotipy.Spotify(auth=token)
    results = spotify.current_user_top_artists()
    # pprint.pprint(results)
    
    return generate_array(results, limit)


def user_recent_tracks():
    os.system('clear')
    limit = 20
    username = ''
    scope = 'user-read-recently-played'
    token = util.prompt_for_user_token(username, scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)
    spotify = spotipy.Spotify(auth=token)
    results = spotify.current_user_recently_played()
    # pprint.pprint(results)
    
    return generate_array(results, limit)


def recommend_top_tracks():
    os.system('clear')

    top_tracks = user_top_tracks()
    limit = 15

    track_attributes = calc_avg_features(top_tracks)
    targets = [at[1] for at in track_attributes]

    # results = spotify.recommendations(seed_tracks=top_tracks, limit=limit)
    results = spotify.recommendations(seed_tracks=top_tracks, limit=limit,
    target_acousticness=targets[0], target_danceability=targets[1], target_duration_ms=targets[2],
    target_energy=targets[3], target_instrumentalness=targets[4], target_key=targets[5],
    target_liveness=targets[6], target_loudness=targets[7], target_mode=targets[8],
    target_speechiness=targets[9], target_tempo=targets[10], target_time_signature=targets[11],
    target_valence=targets[12])
    # pprint.pprint(results)

    for i in range(0, limit):
        print results['tracks'][i]['artists'][0]['name'] + " - " + results['tracks'][i]['name']
    press_to_go_back(1)


def recommend_top_artists():
    os.system('clear')

    top_artists = user_top_artists()
    limit = 15

    # results = spotify.recommendations(seed_artists=top_artists, limit=limit)
    results = spotify.recommendations(seed_artists=top_artists, limit=limit,
    target_acousticness=targets[0], target_danceability=targets[1], target_duration_ms=targets[2],
    target_energy=targets[3], target_instrumentalness=targets[4], target_key=targets[5],
    target_liveness=targets[6], target_loudness=targets[7], target_mode=targets[8],
    target_speechiness=targets[9], target_tempo=targets[10], target_time_signature=targets[11],
    target_valence=targets[12])
    # pprint.pprint(results)

    for i in range(0, limit):
        print results['tracks'][i]['artists'][0]['name'] + " - " + results['tracks'][i]['name']
    press_to_go_back(1)


def recommend_top_tracks_and_artists(): # not working cuz 5 seeds limit...
    os.system('clear')
    
    top_tracks = user_top_tracks()
    top_artists = user_top_artists()
    limit = min(len(top_tracks), len(top_artists))

    results = spotify.recommendations(seed_artists=top_artists, seed_tracks=top_tracks, limit=limit)
    pprint.pprint(results)
    press_to_go_back(1)


def reset_user():
    os.system('clear')
    dir_name = os.path.dirname(os.path.realpath(__file__))
    file_list = os.listdir(dir_name)
    flag = 0

    for item in file_list:
        if item.startswith('.cache'):
            os.remove(os.path.join(dir_name, item))
            flag = 1
    
    if flag:
        print "User(s) removed with success!"
    press_to_go_back(1)
    

def exec_menu(choice, menu_id):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions[menu_id]['menu']()
    else:
        if ch not in menu_actions[menu_id]:
            print 'Invalid selection, please try again.\n'
            menu_actions[menu_id]['menu']()
        else:
            menu_actions[menu_id][ch]()
    return


def press_to_go_back(menu_id):
    raw_input('>> Press to go back to menu')
    os.system('clear')
    menu_actions[str(menu_id)]['menu']()


# Back to main menu
def back():
    menu_actions['1']['menu']()

 
# Exit program
def exit():
    sys.exit()


# Menu definition
menu_actions = {
    '1' : {
        'menu': recommendations_menu,
        '1': recommend_top_tracks,
        '2': recommend_top_artists,
        '3': recommend_top_tracks_and_artists,
        '8': reset_user,
        '0': exit,
    },
}


if __name__ == '__main__':
    recommendations_menu()