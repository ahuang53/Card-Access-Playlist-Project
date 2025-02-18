//Attaches event to the form, .introform
const inputEl = document.querySelector('.introform input[type="text"]');

//Listens for enter button to be pushed
inputEl.addEventListener("keydown", event => {
    if(event.key === 'Enter'){

        event.preventDefault(); //prevents refresh
        const formEl = document.querySelector('.introform');
        const formData= new FormData(formEl); //obj with all form data
        const loading = document.getElementById('loading'); //loading spinner
        const error = document.getElementById('badge-error');
        const data = Object.fromEntries(formData); //JSON obj
        console.log(formData);
        console.log(data);

        loading.style.display = "block"; //show spinner

        //fetch api convert to json
        fetch('/intro-id', { 
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json()) //response
        .then(data => {
            console.log(data);
            formEl.reset();
            if(data.student_name != 'error'){
              document.getElementById("responseText").innerText = ("Welcome "+ data.student_name);  
              error.style.display = 'none';
            }
            else{ 
                error.style.display = 'block'
            }
            loading.style.display = 'none'; //hide spinner
        }) //data
        .catch(error => console.log(error)); //error
    }
});

