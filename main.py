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
    
    #Operation Mode
    while(1):
        
        print("Please indicate the Operation Mode(Intro for Introduction, Play for playlist mode, Search for searching):")
        op_mode = input()
        if(op_mode.strip().lower() == 'search'): #Search for sng mode
            #Song searching
            while(1): #Searching continues until requests end
                found = sg.track_select(genius) #Found is the correct song
                local_playlist.append(store_song(found)) #Add song to local playlist
                print("Do you want to continue?")
                finish = input()
                if(finish.strip().lower() == 'no'):
                    break
                elif(finish.strip().lower() == 'yes'):
                    continue
        elif(op_mode.strip().lower() == "play"):
            if(len(local_playlist) == 0):
                print('Error: Playlist is empty. Please add songs to the playlist before proceeding\n')
                continue
            mp.vlc_play(local_playlist)
        #elif(op_mode.strip().upper() == "INTRO"): intromode needs student ids and an assigned song 
        elif(op_mode.strip().lower() == "exit"):
            break

if __name__ == "__main__":
    main()
