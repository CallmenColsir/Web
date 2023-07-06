const form = document.getElementById("form");
const username = document.getElementById("username");
const password = document.getElementById("password");
const errorMessage = document.querySelector('.errorMessages');

// check error-input
form.addEventListener("submit", (e) => {

    if(username.value === ""){
        e.preventDefault();
        alert("Please enter Username!");
    }
    else if(password.value === ""){
        e.preventDefault();
        alert("Please enter Password!");
    }

});