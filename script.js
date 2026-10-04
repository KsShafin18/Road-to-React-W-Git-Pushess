
// let er kaj kam 
let aboutBtn = document.getElementById("about_section")
aboutBtn.onclick = function() {
    viewAbout()
}

let homeBtn =document.getElementById("home_page")
homeBtn.onclick = function() {
    viewHome()
}

// funtions er kaj kam
function viewAbout(){
    console.log('click ta kaj korse')
    window.location.href = "about.html"
}

function viewHome() {
    window.location.href ="index.html"
}

