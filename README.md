# datSound

Music Recommender System based on Spotify's API and AI techniques.
Project done for MSc - AI course.

Tracks, Events and New Releases (Albums) are recommended based on User's Spotify history.

# Installation

It's a CLI application and all we used was Python (2.7 version).

Apart from Python 2.7 being required to run, app dependencies can be met by doing the following command:

```
$ pip install -r requirements.txt
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

After it, just needs to copy the url on the address bar, which looks like this:

`http://localhost/?code=AQDzB2XUu0dDBRLKivEA-e6GOqHB0IC4mUV1-SMLCrXKrj1tVPVp91MngWMYHbL (...)`

And paste it on the app prompt on the terminal here:

`Enter the URL you were redirected to:`
