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

    #Data Structures
    results = dict() #Stores search results

    #Search for Artist
    print("Enter the song name: ") 
    track_q = input() #inputs
    #print("Enter the artist's name(leave blank if unknown): ")
    #art = input()

    #print("\nThis is {} by {}".format(track,art))
    name = sp.search(track_q, 3, 0,'track') #Outputs a Dictonary Object 
    items_list = name['tracks']['items'] #track details as list obj 
    print(len(name['tracks']['items']))
    
    for i in range(0,len((items_list))): #Runs through top 3 results
        #print("-------------------\n")
        results[items_list[i]['album']["name"]] =( #Name of song searched
        items_list[i]['artists'][0]['name'] ) #Name of artist
        #print((items_list[i]['album']["name"])) #Name of song searched
        #print(" [Album obj] \n")
        #print("-_-_-_-_-_-_-_-_\n")
        #print(items_list[i]['artists'][0]['name']) #name of artist
    print(results)

if __name__ == "__main__":
    main()
