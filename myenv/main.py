"""
This is the main file for this project.

"""

import spotipy #Python library for using spotify data 
from spotipy.oauth2 import SpotifyClientCredentials #Authenticating API
import creds #Stores API keys

"""
Redirect uri: http://localhost:3000/callback #URI that calls back to after authenticating


"""

def main():

    #Authentication
    auth_manager = SpotifyClientCredentials(client_id =creds.client_id, client_secret = creds.client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    #Search for Artist
    name = sp.album("https://open.spotify.com/track/7fBv7CLKzipRk6EC6TWHOB?si=197ecaec67b84c33")
    print(name)


if __name__ == "__main__":
    main()
