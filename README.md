# Card-Access-Playlist-Project #
This is a repository for the Card Access Controlled X-Music Playlist URP project for the Mercer XLab.

## Project Description & Workflow 
Students will be given an opportunity to enter any song of their choice upon entering the Mercer Lab, which will be mixed and play alongside anyone else who is in the room. This will serve to bring a sense of personalization and liveliness to the lab.

1. Students will type in the name and artist for their desired song, which will be searched online to find the most popular results.
2. A confirmation screen for a series of results will pop up, and the student will choose yes or no.
3. The song will be checked for licensing issues and appropriate lyrics before being accepted. If not, an error message will appear and the student will have to select a new song.
4. Once the song is accepted, it will be stored in the local playlist and played when if it is up.

## Additional Features
Introduction Mode - in a student's chosen max set of 3 songs, a small clip of one of those songs is played. This is played when they walk in, and no other music is playing while this mode is on.

Playlist Mode - Every student that enters will have their song added to a shuffled playlist. It will play continuously as long as there are songs in the list. If there are no songs in the playlist, it will shut off until a new student walks in. 

Shuffling = TBD

Manual Shutoff - When selecting an operational mode, enter the term 'exit' to end the program. 

### Installation

1. Make sure to have VLC installed on the system
2. Clone the repository from GitHub
3. Activate the virtual environment and run the program. (Note, this program was developed on Linux)

**To reinstall the virtual environment, steps are below:

#### Unix Systems (macOS & Linux)
2.1. Navigate to your project director:
`cd /your/path/`

2.2. Create a virtual env:
`python3 -m venv myenv`

2.3. Activate the virtual environment:
`source myenv/bin/activate`

2.4. Deactivate it with:
`deactive`

3. Download the dependencies to the virtual environment with:
`pip install -r requirements.txt`

### Credits

Data from Genius API was used to search for and retrieve song information:
- https://docs.genius.com/

Some HTML and CSS files were obtained from CoreyMSchafer:
- https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog

This project was developed using Bootstrap:
- https://getbootstrap.com/

### Additional Controls
- To register songs for an ID on Intro Mode, go to https://songpicker.ecse.rpi.edu
