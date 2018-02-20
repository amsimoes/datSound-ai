# datSound

Music Recommender System based on Spotify's API and AI techniques.
Project done for MSc - AI course.

Authors: [António Simões](https://github.com/amsimoes) & [Igor Rodrigues](https://github.com/ElRoggo)

Tracks, Events and New Releases (Albums) are recommended based on User's Spotify history.

# Overview

It's a CLI application and all we used was Python (2.7 version).

Interacting with the application is pretty simple, using only numerical input (0-9).

Here is the initial menu:

<img align="center" width="280" height="200" src="https://i.imgur.com/igvd7ne.png" alt="menu"/>


# Examples

For Track recommendations there's 5 ways to calculate the suggestion, below it's one of them:
<p align="center">
<img src="https://i.imgur.com/9sfEdyl.png" height="300" width="498" alt="Tracks Recommendation"/>
</p>

For Events recommendations, there's 3 different options to rely on (only works for events in Portugal and users with Portugal as country defined on Spotify account settings):
<p align="center">
<img src="https://i.imgur.com/O0ygXRB.png" alt="Events Recommendation"/>
</p>

For new releases based on Top Tracks (only option available):
<p align="center">
<img src="https://i.imgur.com/BT8hAH4.png" alt="New Releases Recommendation"/>
</p>


# Installation

Apart from Python 2.7 being required to run, app dependencies can be met by doing the following command:

```
$ cd agent
# pip install -r requirements.txt
```

# Running

Running and exploring the application is naturally intuitive.

```
$ cd agent
$ python2 agent.py
```

Navigation inside the menus is done through number inputs (0 - 9).

# App Authorization

On a first run of our application, user will be prompted with a authorization link which will redirect to a Spotify Web Login.
User shall login and authorize our application and it will be redirect to our callback host (localhost empty page).

Afterwards, user just needs to copy the url on the address bar, which looks like this:

`http://localhost/?code=AQDzB2XUu0dDBRLKivEA-e6GOqHB0IC4mUV1-SMLCrXKrj1tVPVp91MngWMYHbL (...)`

And paste it on the app prompt on the terminal here:

`Enter the URL you were redirected to:`
