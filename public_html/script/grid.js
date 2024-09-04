const displayBox = document.getElementById("display-box");
const displayImg = document.getElementById("display-image");
const displayTxt = document.getElementById("display-text");

const grids = document.getElementsByClassName("page-grid");

const gridBoxes = grids[0].getElementsByClassName("inner-box");

const setGridActions = () => {
    for(var i = 0; i < gridBoxes.length; i++) {
        gridBoxes[i].addEventListener("click", gridClick);
    }
    /*
    user.addEventListener("click", linkButton);
    home.addEventListener("click", linkButton);
    feat.addEventListener("click", linkButton);
    actv.addEventListener("click", linkButton);
    futr.addEventListener("click", linkButton);
    
    drop.addEventListener("click", stopProp);*/
};



function gridClick(event) {
    displayBox.style.display = "block";
    
    var img = event.currentTarget.getElementsByTagName("img")[0];
    var txt = event.currentTarget.getElementsByClassName("grid-text")[0];
    
    if(img !== null) {
        displayImg.src = img.src;
    }
    
    if(txt !== null) {
        displayTxt.innerText = txt.innerText;
    }
};



setGridActions();
