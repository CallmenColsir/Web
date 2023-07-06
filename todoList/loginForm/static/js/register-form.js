const username = document.getElementById("username");
const email = document.getElementById("email");
const pw1 = document.getElementById("password1");
const pw2 = document.getElementById("password2");
const form = document.getElementById("form");

form.addEventListener("submit", (e) => {
    if(username.value.length < 6){
        e.preventDefault();
        alert("Username must be atleast 6 letters!");
    }
    else if(email.value === ""){
        e.preventDefault();
        alert("Pleas enter Email!");
    }
    else if(pw1.value.length < 8){
        e.preventDefault();
        alert("Password must be atleast 8 letters!");
    }
    else if(pw2.value === ""){
        e.preventDefault();
        alert("Please Confirm your Password!");
    }
    else if(pw1.value.length >= 8){
        if(!(pw1.value === pw2.value)){
            e.preventDefault();
            alert("Password does not match!");
        }
    }
});