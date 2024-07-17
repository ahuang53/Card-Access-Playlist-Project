'''
This file contains all the function related to playback, shuffling,
and other music player related functions
'''

import os
import vlc #Music player
from time import sleep #Used in introduction mode

'''
This function below searches for a file in a directory by name
'''
def search_file(directory,file_name):
    for filename in os.listdir(directory):
        if filename.startswith(file_name):
            return os.path.join(directory, filename)
    return None


'''
This function belows run the VLC media player to play a specific file.
It takes in the hash id of the file name
'''
def vlc_play(hash_id):
    vlc_path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
    file_path = search_file(os.getcwd(),hash_id)

    # Create a VLC instance with the specified path
    instance = vlc.Instance()

    # Sets the media player on the specifc file
    media_player = instance.media_player_new()
    media = instance.media_new(file_path)
    media_player.set_media(media)

    # Start playing the stream
    media_player.play()
    sleep(5)

    if(media_player.is_playing()):
        print("Playing song...")
    while media_player.is_playing():
        sleep(1)
    if(media_player.is_playing() != 1):
        print("Song has ended...")