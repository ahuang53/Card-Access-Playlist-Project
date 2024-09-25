"""
This file contains all the functions relating to selection, 
searching, and checking the lyric of a song.
"""
#Third-party imports
import requests.exceptions #Handles search function timeouts

"""
This function below performs the search function for the project 
Takes in the Genius API obj to access the LibaryGenius search method
Returns True if search is successful, False if not 
"""
def song_search(genius_obj,track,art):  
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
    

"""
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
"""