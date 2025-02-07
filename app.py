"""
This is the main flask file for this project
"""

#Flask imports
from flask import Flask, request, url_for, render_template,jsonify

#Backend imports
import main

app = Flask(__name__)

data = [
        {'author':'michael',
         'title': 'beat it '},
         
         {'author': 'jung kook',
          'title': 'seven'}
          ]

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

#Intro page code input
@app.route("/intro-id", methods = ['POST'])
def intro_id():
    #Get Json data
    data = request.get_json() 
    rfid = data.get('rfid')
    #print(data)
    #print(rfid)
    main.intro_mode(rfid)
    response = {
        'message' : 'data success',
        'received_data': data
    }
    return jsonify(response)
"""
@app.route("/long")
def link():
    return "AHAAAA"

@app.route("/goat")
def put():
    return redirect(url_for("link"))


"""

if __name__ == "__main__":
    app.run(debug = True)