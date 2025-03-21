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
async function checkSession(){
    console.log("Checking Session...")
    const response = await fetch("/playlist-grab", {method: 'GET'});
    const data = await response.json();

    if(data.message !== "No tracks available"){
        //update everything when track is found
        console.log("Track found:", data);
        track_name.textContent = data.title;
        track_img.src = data.image_url;
        artist_name.textContent = data.artist;
        audiosource.src = `${staticpath}${data.id}.mp3`;
        music.load();
    }
    else{
        console.log("No tracks available in session");
    }
}

//Run the check session when a new song is added
document.addEventListener('song_added', () => {
    checkSession();  // Start checking when the page loads
});

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

// Grab new track data
music.addEventListener('ended', async function(){
    console.log("Track ended, checking session again");
    //Tell session to remove entry
    fetch('/playlist-remove', {method: 'POST', 
                              body: JSON.stringify(data)})
    .then(res => res.json())
    .catch(error => console.error('Error:', error));
    await checkSession();
    if(!music.paused){
        music.play();
    }
});

/*
-Need to add, on startup on to this screen, check for entries in the
 session
-IF session entry exists, update the track name, artist name, img, 
and audio src
-If song.end(), rerun check for entry and the whole thing 
*/


// document.addEventListener("DOMContentLoaded", function() {
//     const songLookupInput = document.getElementById("song-lookup");
//     const idInput = document.getElementById("id");
//     const suggestionsList = document.getElementById("suggestions");
//     const form = document.getElementById("songForm");
//     const errorMessage = document.getElementById("error-message");
    
//     let selectedSong = null;

//     // Event listener for updating suggestions when the user types
//     songLookupInput.addEventListener("input", function() {
//         const searchTerm = songLookupInput.value.toLowerCase();
//         updateSuggestions(searchTerm);
//     });

//     // Function to update the suggestions list based on input
//     function updateSuggestions(searchTerm) {
//         fetch('https://songpicker.ecse.rpi.edu/search-song', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ searchTerm }),
//         })
//         .then(response => response.json())
//         .then(data => {
//             //console.log(data);
//             if (data) {
//                 // Clear existing suggestions
//                 suggestionsList.innerHTML = '';
//                 if (searchTerm.length === 0 || data === null) return;

//                 // Filter songs based on the search term
//                 //const filteredSongs = songs.filter(song => song.title.toLowerCase().includes(searchTerm));
//                 // Add filtered songs to the suggestions list
//                 data.forEach(song => {
//                     const li = document.createElement("li");
//                     li.textContent = `${song.title}`;
//                     li.addEventListener("click", function() {
//                         // Set the clicked suggestion in the input fields
//                         songLookupInput.value = song.title;
//                         selectedSong = song;

//                         // Clear suggestions after selection
//                         suggestionsList.innerHTML = '';
//                     });
//                     suggestionsList.appendChild(li);
//                 });
//             }
//         })
//         .catch(error => {
//             console.error('Error:', error);
//         });
//     }

//     // Prevent default form submission and validate input
//     form.addEventListener("submit", function(event) {
//         event.preventDefault();
        
//         // Validate the form inputs
//         const idValue = idInput.value;
//         const searchValue = songLookupInput.value;

//         if(idValue == ''){
//             errorMessage.textContent = "Please enter your RCSID";
//         }else if (searchValue !== selectedSong.title) {
//             errorMessage.textContent = "Please select a valid song from the suggestions.";
//         } else {
//             //check if selected song is explicit
//             errorMessage.textContent = "Loading...";
//             const songId = selectedSong.id;
//             fetch('https://songpicker.ecse.rpi.edu/is-explicit', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ songId }),
//             })
//             .then(response => response.json())
//             .then(isExplicit => {
//                 //console.log(isExplicit);
//                 if (isExplicit) {
//                     errorMessage.textContent = "That song is explicit. Please choose a clean one."
//                     //clear all textboxes
//                     songLookupInput.value = '';
//                 }else{
//                     errorMessage.textContent = ''; // Clear the error message
//                     // Form submission logic
//                     let xhr = new XMLHttpRequest();
//                     xhr.open('POST', 'queryusersongs.php', true);
//                     xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
//                     xhr.onload = function() {
//                         if (xhr.status == 200) {
//                             console.log("ResponseText: "+xhr.responseText);
//                         } else {
//                             console.error('Request failed. Status: ' + xhr.status);
//                         }
//                     };

//                     xhr.onerror = function() {
//                         console.error('Request failed');
//                     };
//                     let params = 'rcsid='+idValue+'&songid='+selectedSong.id;
//                     xhr.send(params);

//                     //clear all textboxes
//                     songLookupInput.value = '';
//                     idInput.value = '';
//                     alert("Thank you for entering a song!");
//                 }
//             }) 
//         }
//     });
// });
