/*
This file handles all the search functions of the playlist
*/

//Modal yes and no buttons 
const yes_song = document.getElementById("yes-song");
const no_song = document.getElementById("no-song");

//Selects the playlist form
const inputEl = document.querySelector('.playlist-form');

//Modal Obj
const modal = new bootstrap.Modal(document.getElementById('song-confirm'));

//Error alert
const error = document.getElementById('song-error'); //error in the song search

//Listens for enter button to be pushed
inputEl.addEventListener("submit", event => {
    event.preventDefault(); //prevents refresh
    const formData= new FormData(inputEl); //obj with all form data
    const loading = document.getElementById('loading'); //loading spinner
    const data = Object.fromEntries(formData); //JSON obj
    console.log(data);

    loading.style.display = "block"; //show spinner

    //fetch api convert to json
    fetch('/playlist-srch', { 
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json()) //response
    .then(data => {
        console.log(data);
        inputEl.reset();//resets form
        if(data.result[0] == false){ //not found
            console.log("Track not found")
            document.getElementById("errorText").innerText ="ERROR: TRACK NOT FOUND" ;
            error.style.display = 'block';
        }
        else{
            //custom event for yes or no buttons of modal
            const event = new CustomEvent("song_confirm", {detail: data.result});
            document.dispatchEvent(event);
    
            error.style.display = 'none'; //pops up modal confirmation screen
            document.getElementById("song_track").innerText = (data.result[0].title +" by " + data.result[0].artist);
            modal.show();
        }
        loading.style.display = 'none'; //hide spinner
    }) 
    .catch(error => console.log(error)); //error
});

//When song confirm event occurs, send data to yes and no button event listeners
document.addEventListener("song_confirm", (event)=>{
    console.log("Sending to modal buttons");
    yes_song.dataset.result = JSON.stringify(event.detail);
    no_song.dataset.result = JSON.stringify(event.detail);
   
});

yes_song.addEventListener('click', ()=>{
    console.log("clicked yes");
    const eventDetail = JSON.parse(yes_song.dataset.result || '{}'); //parse stringify
    if (eventDetail[1] === "inapp") {
        //error for inappropriate song
        console.log(eventDetail[1]);
        document.getElementById("errorText").innerText ="ERROR: INAPPROPRIATE LYRICS" ;
        error.style.display = 'block';
    }
    else{
        //Fetch post request sending data to sqllite db
        fetch('/playlist-track', { 
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify(eventDetail[0])
        })
        .then(res => res.json()) //response
        .then(data => {
            console.log("Response: ",data);
        })
        .catch(error => {
            console.error("Error: ",error)
        });
    }
});

no_song.addEventListener('click', ()=>{
    console.log("clicked no");
    //parse data
    const eventDetail = JSON.parse(no_song.dataset.result || '{}');
    if (eventDetail[1] === "inapp") {
        //error for inappropriate song
        document.getElementById("errorText").innerText ="ERROR: INAPPROPRIATE LYRICS" ;
        error.style.display = 'block';
    }
});

const test = document.getElementById("all_songs");

test.addEventListener('click', ()=>{
    fetch('/playlist-grab', { 
        method: 'GET',
        headers: {
            'Content-Type':'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error=>{
        console.error('Error: ', error)
    });
});