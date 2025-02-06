"""
This is the main flask file for this project
"""

#Flask imports
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

data = [
        {'author':'michael',
         'title': 'beat it '},
         
         {'author': 'jung kook',
          'title': 'seven'}
          ]
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