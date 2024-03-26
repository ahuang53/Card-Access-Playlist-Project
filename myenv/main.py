"""
This is the main file for this project.

"""

import spotipy #Python library for using spotify data 
from spotipy.oauth2 import SpotifyClientCredentials #Authenticating API
import os #Accessing environment variables
from dotenv import load_dotenv

load_dotenv() #Load the env file

def main():

    #Authentication
    auth_manager = SpotifyClientCredentials(client_id =os.getenv('client_id'), client_secret = os.getenv('client_secret'))
    sp = spotipy.Spotify(auth_manager=auth_manager)

    #Search for Artist
    name = sp.search("SPECIALZ",1)
    print(name['tracks']['name'])


if __name__ == "__main__":
    main()
