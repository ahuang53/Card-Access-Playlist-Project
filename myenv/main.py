"""
This is the main file for this project.

"""
import os #Accessing environment variables
from dotenv import load_dotenv

import lyricsgenius as lg

load_dotenv() #Load the env file
def main():

    #Authentication
    genius = lg.Genius(os.getenv('GENIUS_ACCESS_TOKEN')) #Genius API Obj 

    #Search for Artist & Track
    while(1):
        print("Enter the song name: ") 
        track = input() 
        print("\nEnter the artist's name(leave blank if unknown): ")
        art = input()
        
        if (track != "" and art != ""): #both track and artist are inputted
            query = genius.search_song(track,art) #search for song
            if((query!= None)): #Error Check
                print("\n\n" + query.full_title)
            else:
                print("\nERROR: Track was not found") #Error
        elif (track != ""): #only track is inputted
            query = genius.search_song(track)
            if((query != None)): #Error Check
                print("\n\n" + query.full_title)
            else:
                print("\nERROR: Track was not found")
        elif (art != ""): #only artist is inputted
            print("\nERROR: Track was not found")
        else: #nothing is inputted 
            print("\nERROR: Track was not found")
        
        #Confirmation screen
        print("\nIs this the correct song? Yes or no") 
        confirm = input()
        if(confirm.strip().lower() == "yes"):
            break

    print("Hello")

    
if __name__ == "__main__":
    main()
