'''
This file contains all the function related to playback, shuffling,
and other music player related functions
'''

import os
import vlc #Music player
from time import sleep #Used in introduction mode
import random #Shuffling

'''
This function below searches for a file in a directory by name
'''
def search_file(directory,file_name):
    for filename in os.listdir(directory):
        if filename.startswith(file_name):
            return os.path.join(directory, filename)
    return None

'''
This function below runs the VLC media player to play the entire playlist of
track.
It takes in the local playlist list of track objects. 
'''
def vlc_play(local_playlist):
    while(local_playlist): #Runs through all songs in local playlist
        current_track = local_playlist.pop(0)
        file_path = search_file(os.getcwd(),current_track.get_ID()) 

        #Stop flag for ending the playback
        stop_flag = False

        # Create a VLC instance with the specified path
        instance = vlc.Instance()

        # Sets the media player on the specifc file
        media_player = instance.media_player_new()
        media = instance.media_new(file_path)
        media_player.set_media(media)

        # Start playing the stream
        media_player.play()
        print("Playing track: "+current_track.get_title())

        #Stop and pause function
        while(stop_flag != True):
            playback = input()
            if(playback.strip().lower() == 's'):
                media_player.stop()
                stop_flag = True
                print("Track has stopped...")
            elif(playback.strip().lower() == 'p'):
                media_player.pause()
                print("Track has been paused...")
            elif(playback.strip().lower() == 'sh'):
                random.shuffle(local_playlist)
                print("Playlist has been shuffled...")
    print("Playlist has ended...")