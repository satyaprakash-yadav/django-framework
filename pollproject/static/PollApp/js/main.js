let eyeicon = document.getElementById("eyeicon")
let password = document.getElementById("password")


eyeicon.onclick = function(){
    if(password.type == "password"){
        password.type = "text"
        eyeicon.className = "bi bi-eye-fill"
    }else{
        password.type = "password"
        eyeicon.className = "bi bi-eye-slash-fill"
    }
}