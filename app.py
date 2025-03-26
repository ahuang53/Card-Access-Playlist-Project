"""
This is the main flask file for this project
"""

#Flask imports
from flask import Flask, request, render_template,jsonify, session
from flask_session import Session

from dotenv import load_dotenv
import os

#Backend imports
import main

app = Flask(__name__)
load_dotenv()
app.config['SESSION_TYPE'] = os.getenv("SESSION_TYPE")
app.config['SESSION_PERMANENT'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Session(app)

#Main pages
@app.route("/")
@app.route("/home")
def home():
    if 'queue' not in session:
        session['queue'] = []  # Initialize only if not set
        session.modified = True  # Not required here but useful when modifying later
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
    if 'queue' not in session:
        session['queue'] = []  # Initialize only if not set
    return render_template("playlist.html")

#Intro page search
@app.route("/intro-id", methods = ['POST'])
def intro_id():
    #Get Json data
    data = request.get_json() 
    name = main.intro_mode(data.get('id').strip()) #Gets badge 
    response = {
        'message' : 'data success',
        'student_name': name
    }
    return jsonify(response)

#Playlist page search
@app.route("/playlist-srch", methods = ['POST'])
def playlist_search():
    #Get Json data
    data = request.get_json() 
    search_result = main.searching(data.get('searchTerm',''))
    response = {
        'message' : 'data success',
        'received_data': data,
        'result' : search_result,
    }
    return jsonify(response)

#Playlist page search
@app.route("/is-explicit", methods = ['POST'])
def explicit():
    #Get Json data
    data = request.get_json() 
    result = main.check_explicit(data.get('selectedSong',''))
    response = {
        'message' : 'data success',
        'received_data': data,
        'result' : result,
    }
    return jsonify(response)

#Get all tracks in database
@app.route("/playlist-grab-all", methods = ['GET'])
def get_playlist():
    return jsonify((session['queue']))

#Get oldest entry in the track
@app.route('/playlist-grab', methods= ['GET'])
def get_track():
    if(len(session['queue'])):
        latest_track = session['queue'][0]
        return jsonify(latest_track)
    else:
        return jsonify({'message':'Playlist was empty'})
    
# Add a track to the playlist
@app.route('/playlist-track', methods=['POST'])
def add_track():
    if 'queue' not in session:
        session['queue'] = []  # Initialize queue as empty list

    data = request.json
    new_track = {'id': data.get('id'),
                 'image_url': data.get('header_image_url'),
                 'title': data.get('title'),
                 'artist': data.get('artist_names')}

    if(new_track not in session['queue']):
        #Store track in session as dictionary
        session['queue'].append(new_track)
        session.modified = True
        return jsonify({"message": "Song added"})
    else:
        return jsonify({"message":"Track already exists"})

#Remove latest entry in queue
@app.route('/playlist-dequeue', methods=['POST'])
def remove_track():
    if(len(session['queue'])):
        session['queue'].pop(0)
        return jsonify({'message':'Track was removed'})
    else:
        return jsonify({'message':'Playlist is empty'})

if __name__ == "__main__":
    app.run(debug = True)

