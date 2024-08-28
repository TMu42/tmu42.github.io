
const user = document.getElementById("usr");
const hmbg = document.getElementById("hamburger");
const menu = document.getElementById("menu-bar");
const drop = document.getElementById("hamburger-drop-menu");
const body = document.getElementById("body");

const setActions = () => {
    user.setAttribute("onclick", "location.href='https://github.com/TMu42';");
    
    hmbg.addEventListener("click", toggleHamburger);
    drop.addEventListener("click", stopProp);
    
    document.addEventListener("click", hideHamburger);
    
    //hmbg.setAttribute("onclick", "toggleHamburger();");
    
    //body.setAttribute("onclick", "hideHamburger();");
};


function toggleVisible(element) {
    if(element.style.display === "block") {
        element.style.display = "none";
    } else {
        element.style.display = "block";
    }
};


function toggleHamburger(event) {
    event.stopPropagation();
    
    toggleVisible(drop);
    
    if(hmbg.innerHTML === '☰') {
        hmbg.innerHTML = 'x';
    } else {
        hmbg.innerHTML = '☰';
    }
};


function hideHamburger(event) {
    drop.style.display = "none";
    
    if(hmbg.innerHTML === '☰') {
        hmbg.innerHTML = 'x';
    } else {
        hmbg.innerHTML = '☰';
    }
};


function stopProp(event) {
    event.stopPropagation();
}


setActions();
