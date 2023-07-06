const inputForm = document.getElementById("input-form");
const item = document.getElementById("item");

inputForm.addEventListener("submit", (e) => {
    if(item.value === "" || item.value === null){
        e.preventDefault();
        alert("Please enter Sth!");
    }
});