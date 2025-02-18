//Attaches event to the form, .introform
const inputEl = document.querySelector('.playlist-form');

//Modal Obj
const modal = new bootstrap.Modal(document.getElementById('song-confirm'));

//Listens for enter button to be pushed
inputEl.addEventListener("submit", event => {
    event.preventDefault(); //prevents refresh
    const formEl = document.querySelector('.playlist-form');
    const formData= new FormData(formEl); //obj with all form data
    const error = document.getElementById('song-error'); //error in the song search
    const loading = document.getElementById('loading'); //loading spinner
    const data = Object.fromEntries(formData); //JSON obj
    console.log(formData);
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
        formEl.reset();//resets form

        if(data.result[0] == false){ //makes error message appear 
            if(data.result[1] == "inapp"){
                document.getElementById("errorText").innerText = "ERROR: INAPPROPRIATE LYRICS";
            }
            else if(data.result[1] == "none"){
                document.getElementById("errorText").innerText = "ERROR: TRACK NOT FOUND";
            }
            error.style.display = 'block';
        }
        else{
            error.style.display = 'none';
            document.getElementById("song_track").innerText = (data.result[0] +" by " + data.result[1]);
            modal.show();
            
        }
        //Next time, make model fully functional

        loading.style.display = 'none'; //hide spinner
    }) //data
    .catch(error => console.log(error)); //error
});

