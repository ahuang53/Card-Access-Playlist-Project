"""
This is the main flask file for this project
"""

#Flask imports
from flask import Flask, request, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy

#Backend imports
import main

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playlist.db'  #SQLite file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #Turn off tracking to save resources

db = SQLAlchemy(app)

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID
    title = db.Column(db.String(200), nullable=False)  # Song title
    artist = db.Column(db.String(200), nullable=False)  # Artist name
    def to_dict(self):
        return {"id": self.id, "title": self.title, "artist": self.artist}
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


if __name__ == "__main__":
    app.run(debug = True)