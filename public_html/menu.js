
const user = document.getElementById("usr");
const home = document.getElementById("home");
const hmbg = document.getElementById("hamburger");
const menu = document.getElementById("menu-bar");
const drop = document.getElementById("hamburger-drop-menu");
const body = document.getElementById("body");

const setActions = () => {
    user.addEventListener("click", linkButton);
    home.addEventListener("click", linkButton);
    drop.addEventListener("click", stopProp);
    
    document.addEventListener("click", toggleHamburger);
};


var hamburger = false;

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
    const burgerChild = [hmbg, ...getDescendants(hmbg)];
    const dropChild   = [drop, ...getDescendants(drop)];
    
    if(burgerChild.includes(event.target)) {
        if(hamburger) {
            hideHamburger(event);
        } else {
            showHamburger(event);
        }
    } else if(!dropChild.includes(event.target)) {
        hideHamburger(event);
    }
};


function hideHamburger(event) {
    drop.style.display = "none";
    
    hmbg.innerHTML = '☰';
    
    hamburger = false;
};


function showHamburger(event) {
    drop.style.display = "block";
    
    hmbg.innerHTML = 'x';
    
    hamburger = true;
};


function stopProp(event) {
    event.stopPropagation();
};


function getDescendants(elem, all = []) {
    all.push(...elem.childNodes);
    
    for (const child of elem.childNodes) {
        getDescendants(child, all);
    }
    
    return all;
};


setActions();
