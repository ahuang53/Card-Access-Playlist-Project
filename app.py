"""
This is the main flask file for this project
"""

#Flask imports
from flask import Flask, request, render_template,jsonify, session
from flask_session import Session

from dotenv import load_dotenv
import os
from datetime import datetime
#Backend imports
import main

app = Flask(__name__)
load_dotenv()
app.config['SESSION_TYPE'] = os.getenv("SESSION_TYPE")
app.config['SESSION_PERMANENT'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Session(app)

#Define Track Object
class Track():
    def __init__(self, id, image_url,title,artist):
        self.id = id
        self.image_url = image_url
        self.title = title
        self.artist = artist
        self.timestamp = datetime.now() #Timestamp for sorting in session

    #Convert to dictionary
    def to_dict(self):
        return {
            "id": self.id, 
            "title": self.title, 
            "artist": self.artist, 
            "image_url":self.image_url,
            'timestamp':self.timestamp
            }

# # This will clear the session before the first request is handled
# @app.before_request
# def clear_session_on_startup():
#     session.clear()  # Clears the session

#Main pages
@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/intro")
def intro():
    return render_template("intro.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/playlist")
def playlist():
    session.clear() #Clears session playlist when page loads
    return render_template("playlist.html")

#Intro page search
@app.route("/intro-id", methods = ['POST'])
def intro_id():
    #Get Json data
    data = request.get_json() 
    name = main.intro_mode(data.get('badge')) #Gets badge 
    response = {
        'message' : 'data success',
        'received_data': data,
        'student_name': name
    }
    return jsonify(response)

#Playlist page search
@app.route("/playlist-srch", methods = ['POST'])
def playlist_search():
    #Get Json data
    data = request.get_json() 
    search_result = main.searching(data.get('song'),data.get('author'))
    response = {
        'message' : 'data success',
        'received_data': data,
        'result' : search_result,
    }
    return jsonify(response)

#Get all tracks in database
@app.route("/playlist-grab-all", methods = ['GET'])
def get_playlist():
    return jsonify(dict(session))

#Get oldest entry in the track
@app.route('/playlist-grab', methods= ['GET'])
def get_track():
    if session:
        #Grab oldest track
        latest_track = min(session.values(), key=lambda track: track['timestamp'])
        #session.pop(latest_track.get('id'))
        return jsonify(latest_track)  # Return the latest track
    else:
        return jsonify({"message": "No tracks available"})

# Add a track to the playlist
@app.route('/playlist-track', methods=['POST'])
def add_track():
    data = request.json
    data_id = data.get('id')
    if(data_id not in session):
        new_track = Track(id=data.get('id'), 
                            image_url=data.get('header_image_url'),
                            title=data.get('title'), 
                            artist=data.get('artist')
                            )
        #Store track obj in session as dictionary
        session[data_id] = new_track.to_dict()

        #Sort entry by timestamp
        session_entries = list(session.values())
        session_entries.sort(key = lambda x: x['timestamp'])
        for i, track in enumerate(session_entries):
            session[track['id']] = track  # Reassign sorted track back to session

        return jsonify({"message": "Song added"})
    else:
        return jsonify({"message":"Track already exists"})

@app.route('/playlist-remove', methods=['POST'])
def remove_track():
    data_id = (request.json).get('id')
    if(data_id in session):
        session.pop(data_id)
        return jsonify({'message':'Track was removed'})
    else:
        return jsonify({'message':'Track was not found'})



if __name__ == "__main__":
    app.run(debug = True)

