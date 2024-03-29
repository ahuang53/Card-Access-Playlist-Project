# Card-Access-Playlist-Project #
This is a repository for the Card Access Controlled X-Music Playlist URP project for the Mercer XLab.

## Project Description & Workflow 
Students will be given an opportunity to enter any song of their choice upon entering the Mercer Lab, which will be mixed and play alongside anyone else who is in the room. This will serve to bring a sense of personalization and liveliness to the lab.

1. Students will type in the name and artist for their desired song, which will be searched online to find the most popular results.
2. A confirmation screen for a series of results will pop up, and the student will choose yes or no.
3. The song will be checked for licensing issues and appropriate lyrics before being accepted. If not, an error message will appear and the student will have to select a new song.
4. Once the song is accepted, it will be locally stored in a Box folder corresponding to the student's name and RPI ID.
5. The songs will either be played like normal, or used for data in other modes. 

## Additional Features
Introduction Mode - in a student's chosen max set of 3 songs, a small clip of one of those songs is played. This is played when they walk in, and no other music is playing while this mode is on.

Playlist Mode - Every student that enters will have their song added to a shuffled playlist. It will play continuously as long as there are songs in the list. If there are no songs in the playlist, it will shut off until a new student walks in. 

Shuffling = TBD

Manual Shutoff - TBD

### Credits

This project uses data obtained from the Spotify API to search for and retrieve song information.
- [Spotify Developer](https://developer.spotify.com/)


https://spotipy.readthedocs.io/en/2.22.1/#getting-started


### Installation
- Install virtual environment to manage depencencies:
 Markup: pip install virtualenv



