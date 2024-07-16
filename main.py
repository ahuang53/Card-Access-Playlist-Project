"""
This is the main file for this project.

"""
#Standard Library imports
import os #Accessing environment variables
import vlc #Music player
from time import sleep #Used in introduction mode
from dotenv import load_dotenv 
import hashlib #Hash function 

#Third-party imports
import lyricsgenius as lg #Genius API search
import requests.exceptions #Handles search function timeouts

#Module imports
import song as sg #Song search and check related functions

load_dotenv() #Load the env file

'''
This function below generates a hash value based on song's full title
'''
def hash_string(input_string):
    hash_val = hashlib.sha256(input_string.encode()).hexdigest()
    return hash_val

'''
This function below searches for a file in a directory by name
'''
def search_file(directory,file_name):
    for filename in os.listdir(directory):
        if filename.startswith(file_name):
            return os.path.join(directory, filename)
    return None


def main():
    #Authentication
    genius = lg.Genius(os.getenv('GENIUS_ACCESS_TOKEN')) #Genius API Obj 
    found = sg.track_select(genius) #Found is the correct song
    '''
    #Operation Mode
    print("Please indicate the Operation Mode(I for Introduction, P for playlist mode, S for searching):")
    op_mode = input()
    if(op_mode.strip().upper() == "S"):
        #Song searching
        found = track_select(genius) #Found is the correct song
    '''
    file_path = search_file(os.getcwd(), hash_string(found.full_title))
    print(file_path)

    vlc_path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'

    # Create a VLC instance with the specified path
    instance = vlc.Instance()

    # Replace 'your_stream_url' with the actual URL of the stream you want to play
    media_player = instance.media_player_new()
    media = instance.media_new(file_path)
    media_player.set_media(media)

    # Start playing the stream
    media_player.play()
    sleep(5)

    while media_player.is_playing():
        print("Playing...")
    
    
if __name__ == "__main__":
    main()
