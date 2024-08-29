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


function setCookie(name, value, expiry, path) {
    var keyVal  = name + '=' + value + ';';
    var expires = "";
    var pathStr = "path=/";
    
    if(expiry !== undefined && expiry !== null) {
        expires = "expires=" + expiry + ';';
    }
    
    if(path !== undefined && path !== null) {
        pathStr = "path=" + path + ';'
    }
    
    document.cookie = keyVal + expires + pathStr;
};


function getCookie(name) {
    for(cookie of document.cookie.split(';')) {
        while(cookie[0] == ' ') {
            cookie = cookie.substring(1, cookie.length);
        }
        
        if(cookie.indexOf(name + '=') == 0) {
            return cookie.substring(name.length + 1, cookie.length);
        }
    }
    
    return null;
};


function delCookie(name, path) {
    if(path === undefined || path === null) {
        path = "/";
    }
    
    document.cookie = name + "=; path=" + path
                    + "; expires=Thu, 01 Jan 1970 00:00:00 GMT;";
};
