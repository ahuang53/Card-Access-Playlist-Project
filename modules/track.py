'''
This file is a class file for the track object
Each track object stores a song's title, artist name, and ID
'''
class Track:
    def __init__(self,title,art_name,ID):
        self.title = title
        self.artist = art_name
        self.id = ID
    
    #Accessor Functions
    def get_title(self):
        return self.title
    def get_artist(self):
        return self.artist
    def get_ID(self):
        return self.id
    
    #Modifier Functions
    def set_title(self,value):
        self.title = value
    def set_artist(self,value):
        self.artist = value
    def set_id(self,value):
        self.id = value

    def __str__(self):
        return "{} by {}\nID:{}".format(self.title,self.artist,self.id)
        