'''
This file contains all the function related to playback, shuffling,
and other music player related functions
'''

import os
import vlc #Music player
from time import sleep #Used in introduction mode

# Create a VLC player instance globally so it can be accessed across functions
player = None

'''
This function below searches for a file in a directory by name
'''
def search_file(directory,file_name):
    for filename in os.listdir(directory):
        if filename.startswith(file_name):
            return os.path.join(directory, filename)
    return None

'''
This function below runs the VLC media player to play a selected song
'''
def vlc_intro_play(song_id):
    file_path = search_file("/home/andyh/Downloads/Card-Access-Playlist-Project/songs",song_id) 
    # Create a VLC instance with the specified path
    instance = vlc.Instance()
    # Sets the media player on the speciifc file
    media_player = instance.media_player_new()
    media = instance.media_new(file_path)
    media_player.set_media(media)
    # Start playing the stream
    media_player.play()
    print(media_player.is_playing())
<<<<<<< HEAD
    sleep(7)
=======
    sleep(3)
>>>>>>> 8029670ecc140f8abcb169db18991d7ee177f60a
    media_player.stop()
    print(media_player.is_playing())
#def vlc_stop(media_player)

def vlc_playlist_play(local_playlist):
    while(local_playlist):
        current_track = local_playlist.pop(0)
        print(current_track.id)
<<<<<<< HEAD
        file_path = search_file("/home/andyh/Downloads/Card-Access-Playlist-Project/songs",str(current_track.id)) 
=======
        file_path = search_file(os.getcwd()+"/songs",str(current_track.id)) 
>>>>>>> 8029670ecc140f8abcb169db18991d7ee177f60a
        global player
        # Create a new VLC instance and player
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new(file_path)
        player.set_media(media)

        # Start playing the media
        player.play()
        sleep(2)
        print("Playing track: "+current_track.title)

def vlc_pause():
    global player
    player.pause()

'''
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
<<<<<<< HEAD
'''
=======
'''
>>>>>>> 8029670ecc140f8abcb169db18991d7ee177f60a
