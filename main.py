"""
This is the main backend for this project.

"""
#Standard Library imports
import os #Accessing environment variables
#from dotenv import load_dotenv 
#import hashlib #Hash function 
import random #Shuffling

#Third-party imports
import lyricsgenius as lg #Genius API search
#import mysql.connector #Database for intro mode
#import paramiko #SSH Client
#from sshtunnel import SSHTunnelForwarder
#import dearpygui.dearpygui as dpg #Main library
import requests
from bs4 import BeautifulSoup

#Module imports
import modules.lyric_song_search as sg #Song search and check related functions
#import modules.music_playing as mp #Vlc playback
import modules.BadgeLookup as arts

#Class imports
from modules.track import Track #Track class to store each song's attributes

#Frontend UI imports
#import Ui.gui as ui

#load_dotenv() #Load the env file
"""
'''
This function below generates a hash value based on song's full title
'''
def hash_string(input_string):
    hash_val = hashlib.sha256(input_string.encode()).hexdigest()
    return hash_val
"""


"""
'''
This function below takes in the song obj from lyrics genius and assigns
its attributes to a track object
It will return the track obj
'''
def store_song(song_obj):
    new_track = Track(song_obj.title,song_obj.artist,hash_string(song_obj.full_title))
    return new_track
"""

'''
This functions returns a SQL Database entry using an RCSID
'''
def access_database(id, ssh_client):
    try:
        #Connect to SSH server
        ssh_client.connect(hostname=os.getenv('hostname'), 
                        username=os.getenv('username'), 
                        password=os.getenv('password'))
        #MySQL Command
        id = id.replace("'", "\\'")
        mysql_command = f"""
        mysql -u songuser -p'songuser123!' --silent 2>/dev/null -e "USE songpicker; SHOW TABLES; SELECT * FROM userSongs WHERE rcsid = '{id}';"
        """
        #Read SQL output
        stdin, stdout, stderr = ssh_client.exec_command(mysql_command)
        error = stderr.read().decode()
        if error:
            print("Error:", error)
        else:
            result = stdout.read().decode()
            #print(result)
        row = result.strip().split('\n')
        val = row[1].split('\t')
        print(val)
        return val
    
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        #Close connection
        ssh_client.close()

'''
This functions runs the intro mode when the scanner goes 
'''
def intro_mode(code):
    print("Intro Mode")    
    #Starts SSH client
    #dpg.set_value("wait", "Playing...")
    #ssh_client = paramiko.SSHClient()
    #ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #print(code+"Code")
    print("-----------")
    try: #Looks up student in ARTS
        #(arts.Register(code))
        result = arts.Lookup(code)
        if(result.get('Result')!= 'Allowed'):
            return "error"
        return result.get('Tokens').get('NAME')#the scanner id 
    except Exception as e:
        print(f"An error occured: {e}")
        rcsid = str(code)
    #val = access_database(rcsid,ssh_client)[2]
    #mp.vlc_intro_play(str(val))
    #dpg.set_value("wait", "Waiting...")
    #dpg.set_value("intro_scan", "")

'''
This function runs search function and returns the song dictionaries as an array
'''
def searching(search_term):
    result = sg.song_search(lg.Genius(os.getenv('GENIUS_ACCESS_TOKEN')),
                            search_term)

    #Convert results dictionary to list of song dictionaries
    songObj_list = []
    for item in result.get('hits'):
        songObj_list.append(item['result'])
    
    return songObj_list
    #Remove redundancy of modules and put everything here??


def check_explicit(song_obj):
    #not song_obj, doesnt have to_text for lyrics
    genius_obj = lg.Genius(os.getenv('GENIUS_ACCESS_TOKEN'))
    song_lyrics = genius_obj.search_song(song_obj["title"]).to_text()
    return (sg.lyric_check(song_lyrics))

'''
This function runs the playlist mode 
'''
# def playlist_mode():
#     print("Playlist Mode")
#     current_play_str = "Current Playlist: \n"
#     for track in local_playlist:# Update current playlist 
#             current_play_str += track.title+"\n"
#     dpg.set_value("current_play",current_play_str)
#     print(current_play_str)
#     mp.vlc_playlist_play(local_playlist)
#     print("YES")

# def playlist_control(command):
#     if(command == "play"):
#         mp.vlc_pause()
#     elif(command == "shuffle"):
#         random.shuffle(local_playlist)
    
#https://apex.cct.rpi.edu/apex/f?p=149:76:32764355658653::::: for events
def main():
    #Authentication
    code = 'AE5195F7'
    #print(arts.Register(code))
    #print(arts.Lookup(code))
    #rcsid = arts.Lookup(code)[0] #the scanner id 
    #ui.setup_ui()
    #print( (sg.song_search(lg.Genius(os.getenv('GENIUS_ACCESS_TOKEN'))
    #                        ,"rapture","anita baker")).id)
    

if __name__ == "__main__":
    main()
