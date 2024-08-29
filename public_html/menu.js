
const user = document.getElementById("usr");
const home = document.getElementById("home");
const hmbg = document.getElementById("hamburger");
const menu = document.getElementById("menu-bar");
const drop = document.getElementById("hamburger-drop-menu");
const body = document.getElementById("body");

const setActions = () => {
    user.addEventListener("click", linkButton);
    home.addEventListener("click", linkButton);
//    hmbg.addEventListener("click", toggleHamburger);
    drop.addEventListener("click", stopProp);
    
    document.addEventListener("click", toggleHamburger);
};


function toggleVisible(element) {
    if(element.style.display === "block") {
        element.style.display = "none";
    } else {
        element.style.display = "block";
    }
};


function linkButton(event) {
    const buttonId = event.currentTarget.id;
    
    if (buttonId === "usr") {
        location.href = "https://github.com/TMu42";
    } else if (buttonId === "home") {
        location.href = "https://tmu42.github.io/";
    }
};


function toggleHamburger(event) {
    if(event.target === hmbg) {
        if(hmbg.innerHTML === '☰') {
            showHamburger(event);
        } else {
            hideHamburger(event);
        }
    } else if(!(event.target === drop)) {
        hideHamburger(event);
    }
};


function hideHamburger(event) {
    drop.style.display = "none";
    
    hmbg.innerHTML = '☰';
};


function showHamburger(event) {
    drop.style.display = "block";
    
    hmbg.innerHTML = 'x';
};


function stopProp(event) {
    event.stopPropagation();
}


setActions();
