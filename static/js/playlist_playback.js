/*
This file handles all the logic with the audio player in the playlist page
*/

//All playback elements
const music = document.getElementById("music");
const audiosource = document.getElementById('audiosource');
const pButton = document.getElementById("pButton");
const timeline = document.getElementById("timeline");
const playhead = document.getElementById("playhead");

//All image and text elements
const track_name = document.getElementById('track-name');
const artist_name = document.getElementById('artist-name');
const track_img = document.getElementById('track-img');

//Checks if mouse is dragging playing head or not 
let dragging = false;

//Calculates movement and timing 
function movePlayhead(event) {
    const timelineRect = timeline.getBoundingClientRect();
    let newX = event.clientX - timelineRect.left;
    const timelineWidth = timeline.offsetWidth;

    newX = Math.max(0, Math.min(newX, timelineWidth));
    const newTime = (newX / timelineWidth) * music.duration;

    playhead.style.left = (newX / timelineWidth) * 100 + "%";
    music.currentTime = newTime;
}

//Asynchronous function to check if session isn't empty
async function playTrack(){
    // console.log("Checking Session...")
    const response = await fetch("/playlist-grab", {method: 'GET'});
    const data = await response.json();

    if(data.message !== "Playlist was empty"){
        //update everything when track is found
        track_name.textContent = data.title;
        track_img.src = data.image_url;
        artist_name.textContent = data.artist;
        audiosource.src = `${staticpath}${data.id}.mp3`;
        //load and start track
        music.load();
        music.play();
        pButton.classList.remove("fa-play");
        pButton.classList.add("fa-pause");
    }
}

//Function to check if audio is available to play
function checkAudioState(){
    if(music.paused && music.currentTime === 0){ //audio is not paused or playing
        console.log('Audio player is in ready state')
        playTrack();
    }
    else{
        console.log('Audio player not ready')
    }
}

document.addEventListener("DOMContentLoaded", function() {
    setInterval(checkAudioState,2000); //check if player is ready

    // Play/Pause functionality
    pButton.addEventListener("click", function() {
        console.log("Clicked play"); 
        if (music.paused) {
            music.play();
            pButton.classList.remove("fa-play");
            pButton.classList.add("fa-pause");
        } else {
            console.log("track start");
            music.pause();
            pButton.classList.remove("fa-pause");
            pButton.classList.add("fa-play");
        }
    });

    // Update playhead position
    music.addEventListener("timeupdate", function() {
        if (!dragging) {
            const percent = (music.currentTime / music.duration) * 100;
            playhead.style.left = percent + "%";
        }
    });

    // Click to seek
    timeline.addEventListener("click", function(event) {
        const timelineWidth = timeline.offsetWidth;
        const clickX = event.offsetX;
        const newTime = (clickX / timelineWidth) * music.duration;
        music.currentTime = newTime;
    });

    // Dragging playhead functionality
    playhead.addEventListener("mousedown", function() {
        dragging = true;
        document.addEventListener("mousemove", movePlayhead);
        document.addEventListener("mouseup", function() {
            dragging = false;
            document.removeEventListener("mousemove", movePlayhead);
        });
    });

    // Grab new track data when song ends
    music.addEventListener('ended', async function(){
        console.log("Track ended");
        //Tell session to remove entry

        fetch('/playlist-dequeue', {method: 'POST', })
        .then(res => res.json())
        .catch(error => console.error('Error:', error));
        //Reset player
        music.currentTime = 0;
        music.pause();
        pButton.classList.remove("fa-pause");
        pButton.classList.add("fa-play");
        // if(!music.paused){
        //     music.play();
        // }
    });
});

/*
-Need to add, on startup on to this screen, check for entries in the
 session
-IF session entry exists, update the track name, artist name, img, 
and audio src
-If song.end(), rerun check for entry and the whole thing 
*/

