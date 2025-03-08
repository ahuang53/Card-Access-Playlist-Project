/*
This file handles all the logic with the audio player in the playlist page
*/

const music = document.getElementById("music");
const pButton = document.getElementById("pButton");
const timeline = document.getElementById("timeline");
const playhead = document.getElementById("playhead");

let dragging = false;

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

function movePlayhead(event) {
    const timelineRect = timeline.getBoundingClientRect();
    let newX = event.clientX - timelineRect.left;
    const timelineWidth = timeline.offsetWidth;

    newX = Math.max(0, Math.min(newX, timelineWidth));
    const newTime = (newX / timelineWidth) * music.duration;

    playhead.style.left = (newX / timelineWidth) * 100 + "%";
    music.currentTime = newTime;
}