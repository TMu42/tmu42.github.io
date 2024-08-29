function toggleVisible(element) {
    if(element.style.display === "block") {
        element.style.display = "none";
    } else {
        element.style.display = "block";
    }
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
