"""
This is the main file for this project.

"""

#Imports
import os #Accessing environment variables
from dotenv import load_dotenv

import lyricsgenius as lg #Genius API search

import requests.exceptions #Handles search function timeouts

load_dotenv() #Load the env file

"""
This function below performs the search function for the project 
Takes in the Genius API obj to access the LibaryGenius search method
Returns True if search is successful, False if not 
"""
def search(genius_obj):
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
        return False

def main():

    #Authentication
    genius = lg.Genius(os.getenv('GENIUS_ACCESS_TOKEN')) #Genius API Obj 
    while(1):
        result = search(genius) #Repeat the search engine until correct song is found
        if(result != False):
            print("\nIs this the correct song? Yes or No") 
            confirm = input()
            if(confirm.strip().lower() == "yes"):#Correct song is found
                if(lyric_check(result.to_text()) != 0): #Song is safe
                    print("\nConfirmed: "+result.full_title)
                    break
                else:
                    print("\nERROR: Track is inappropriate")
                    continue
    #Current "result" obj is now the correct song
    #print(correct)

if __name__ == "__main__":
    main()
