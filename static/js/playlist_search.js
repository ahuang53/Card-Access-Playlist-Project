/*
This file handles all the search functions of the playlist
*/

document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById('playlist-form'); //form
    const loading = document.getElementById('loading'); //loading spinner
    const songInput = document.getElementById("song_input");
    const suggestList = document.getElementById("suggestions"); //suggestions list
    const error = document.getElementById("errorText") //error message

    let selectedSong = null; //saves song_obj

    // Event listener for updating suggestions when the user types
    songInput.addEventListener("input", function() {
        if(songInput.value === "") suggestList.innerHTML = '';
        else{
            const searchTerm = songInput.value.toLowerCase();
            updateSuggests(searchTerm);
        }
    });

    // Function to update the suggestions list based on input
    function updateSuggests(searchTerm) {
        fetch('/playlist-srch', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ searchTerm }),
        })
        .then(response => response.json())
        .then(data => {
            //console.log(data);
            if (data) {
                // Clear existing suggestions
                suggestList.innerHTML = '';
                if (searchTerm.length === 0 || data === null) return;

                // Add filtered songs to the suggestions list
                data.result.forEach(song => {
                    const li = document.createElement("li");
                    li.textContent = `${song.full_title}`;
                    li.addEventListener("click", function() {
                        // Set the clicked suggestion in the input fields
                        songInput.value = song.full_title;
                        selectedSong = song;

                        //console.log(song);

                        // Clear suggestions after selection
                        suggestList.innerHTML = '';
                    });
                    suggestList.appendChild(li);
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    input.addEventListener("submit", function(event) {
        event.preventDefault(); //prevents refresh
        loading.style.display = "block"; //show spinner

        // Validate the form inputs
        fetch('/is-explicit', { 
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify({selectedSong})
        })
        .then(res => res.json()) //response
        .then(data => {
            console.log(data.result);
            input.reset();//resets form

            if(data.result == false){ //not found
                console.log("Track not found")
                error.innerText ="ERROR: TRACK IS EXPLICT. PLEASE PICK ANOTHER" ;
            }
            else{
                //Fetch post request sending data to database
                fetch('/playlist-track', { 
                    method: 'POST',
                    headers: {
                        'Content-Type':'application/json'
                    },
                    body: JSON.stringify(selectedSong)
                })
                .then(res => res.json()) //response
                .then(data => {
                    console.log("Response: ",data);
                })
                .catch(error => {
                    console.error("Error: ",error)
                });
                //song is accepted, add to playlist
            }
            loading.style.display = 'none'; //hide spinner
        }) 
        .catch(error => {
            console.log(error);
            error.innerText = "An error occurred, please try again.";
        }) 
        .finally(() => {
            loading.style.display = 'none'; //hide spinner
        });
    });
});


// TEST BUTTONS BELOW, NOT FINAL
const test = document.getElementById("all_songs");

test.addEventListener('click', ()=>{
    fetch('/playlist-grab-all', { 
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

const test2 = document.getElementById("one_song");

test2.addEventListener('click', ()=>{
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

