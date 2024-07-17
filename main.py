"""
This is the main file for this project.

"""
#Standard Library imports
import os #Accessing environment variables
from dotenv import load_dotenv 
import hashlib #Hash function 

#Third-party imports
import lyricsgenius as lg #Genius API search

#Module imports
import lyric_song_search as sg #Song search and check related functions
import music_playing as mp #Vlc playback

#Class imports
from track import Track #Track class to store each song's attributes

load_dotenv() #Load the env file

'''
This function below generates a hash value based on song's full title
'''
def hash_string(input_string):
    hash_val = hashlib.sha256(input_string.encode()).hexdigest()
    return hash_val

'''
This function below takes in the song obj from lyrics genius and assigns
its attributes to a track object
It will return the track obj
'''
def store_song(song_obj):
    new_track = Track(song_obj.title,song_obj.artist,hash_string(song_obj.full_title))
    return new_track

def main():
    #Authentication
    local_playlist = [] #Stores all the local songs being played
    genius = lg.Genius(os.getenv('GENIUS_ACCESS_TOKEN')) #Genius API Obj 
    found = sg.track_select(genius) #Found is the correct song
    print(store_song(found))
    '''
    #Operation Mode
    print("Please indicate the Operation Mode(I for Introduction, P for playlist mode, S for searching):")
    op_mode = input()
    if(op_mode.strip().upper() == "S"):
        #Song searching
        found = track_select(genius) #Found is the correct song
    '''
    #vlc_play(hash_string(found.full_title))
    
    
if __name__ == "__main__":
    main()
