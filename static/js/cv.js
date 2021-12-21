function myFunction(){
    const inpObj = document.getElementById("email");
    if (!inpObj.checkValidity()) {
    document.getElementById("email").innerHTML = inpObj.validationMessage;
    } else {
    document.getElementById("email").innerHTML = "Email is valid!";
       }
}

