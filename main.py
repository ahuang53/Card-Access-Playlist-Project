"""
This is the main file for this project.

"""

#Imports

#Accessing local software imports
import os #Accessing environment variables
import vlc #Music player
from time import sleep #Used in introduction mode
from dotenv import load_dotenv 

#API imports
import lyricsgenius as lg #Genius API search
import requests.exceptions #Handles search function timeouts

#Data imports
import hashlib #Hash function 

load_dotenv() #Load the env file

"""
This function below performs the search function for the project 
Takes in the Genius API obj to access the LibaryGenius search method
Returns True if search is successful, False if not 
"""
def song_search(genius_obj):
    print("\nEnter the song name: ") 
    track = input() 
    print("\nEnter the artist's name(leave blank if unknown): ")
    art = input()
    
    if ( (track != "" and art != "") or track != ""): #track or track with artist
        try: #Error check for function timeout
            query = genius_obj.search_song(track,art) #search for song
        except requests.exceptions.Timeout:
            print("\nTIMEOUT: Track was not found") #Error
            return False #Return to searching
        if((query!= None)): #Error Check for no sound found 
            print("\n"+query.full_title)
            return query #Successful search
        else:
            print("\nERROR: Track was not found") #Error
            return False #Return to searching
    elif (art != ""): #only artist is inputted
        print("\nERROR: Track was not found")
        return False
    else: #nothing is inputted 
        print("\nERROR: Track was not found")
        return False

"""
This function below checks if the lyrics of the selected song is appropriate
The function takes in a string of the song lyrics
Returns True if none of the lyrics match with a list of inappropriate words,
and False if not 
"""
def lyric_check(lyric_str):
    bad_words = set()
    file = open("en.txt",'r') #Inappropriate word list
    for word in file:  
        bad_words.add(word.strip().lower())

    words = lyric_str.split() 
    final_words =set( [word.strip().lower() for word in words]) #Add all lyrics to set
    if(len(final_words.intersection(bad_words)) == 0): #Check matching words
        return True
    else:
        print(final_words.intersection(bad_words))
        return False
    
'''
This function below handles the song selection process.
It will call the search function to look through the database for the specified 
query. Then, if the track passes the lyrics check function, it will return its object.
'''
def track_select(genius):
    while(1):
        result = song_search(genius) #Repeat the search engine until correct song is found
        if(result != False):
            print("\nIs this the correct song? Yes or No") 
            confirm = input()
            if(confirm.strip().lower() == "yes"):#Correct song is found
                if(lyric_check(result.to_text()) != 0): #Song is safe
                    print("\nConfirmed: "+result.full_title)
                    return result
                else:
                    print("\nERROR: Track is inappropriate")
                    continue

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
    found = track_select(genius) #Found is the correct song
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
        sleep(1)
    
    
if __name__ == "__main__":
    main()
