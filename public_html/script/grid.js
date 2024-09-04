const displayBox = document.getElementById("display-box");
const displayImg = document.getElementById("display-image");
const displayTxt = document.getElementById("display-text");

const displayClose = document.getElementById("display-close");

const grids = document.getElementsByClassName("page-grid");

const gridBoxes = grids[0].getElementsByClassName("inner-box");

const setGridActions = () => {
    for(var i = 0; i < gridBoxes.length; i++) {
        gridBoxes[i].addEventListener("click", gridClick);
    }
    
    document.addEventListener("click", closeDisplay);
};



function gridClick(event) {
    var img = event.currentTarget.getElementsByTagName("img")[0];
    var txt = event.currentTarget.getElementsByClassName("grid-text")[0];
    
    if(img !== null) {
        displayImg.src = img.src;
        displayImg.alt = img.src.split('/')[img.src.split('/').length - 1];
    }
    
    if(txt !== null) {
        displayTxt.innerText = txt.innerText;
    }
    
    displayBox.style.display = "block";
};


function closeDisplay(event) {
    const closeChild = [displayClose, ...getDescendants(displayClose)];
    const displChild = [displayBox,   ...getDescendants(displayBox)];
    
    var gridChild = [];
    
    for(var i = 0; i < gridBoxes.length; i++) {
        gridChild = [...gridChild, gridBoxes[i],
                     ...getDescendants(gridBoxes[i])];
    }
    
    if(closeChild.includes(event.target)
    || !(displChild.includes(event.target)
      || gridChild.includes(event.target))) {
        displayBox.style.display = "none";
    }
}


setGridActions();
