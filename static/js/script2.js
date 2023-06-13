document.addEventListener('DOMContentLoaded', function(){
    let another = document.querySelector(".another");
    let gender = document.querySelector(".gender");
    let base = document.querySelectorAll(".base");
    another.addEventListener('click', function(){
        gender.style.visibility = "visible";
    })
    for (let i = 0; i < base.length; i++)
    {
        base[i].addEventListener('click', function(){
            gender.style.visibility = "hidden";
        })
    }
})