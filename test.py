"""
This is the main flask file for this project
"""

#Flask imports
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

data = ["beat it", ""]

@app.route("/")
def home():
    return render_template("home.html", data = data)



"""
@app.route("/long")
def link():
    return "AHAAAA"

@app.route("/goat")
def put():
    return redirect(url_for("link"))


"""

if __name__ == "__main__":
    app.run()