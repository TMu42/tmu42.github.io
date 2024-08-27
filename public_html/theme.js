const favLnk = document.getElementById("favicon-link");

const dark = window.matchMedia("(prefers-color-scheme: dark)");

const titIm0 = document.getElementById("title-image0");
const titIm1 = document.getElementById("title-image1");

const updateTheme = () => {
    
    if(dark.matches) {
        favLnk.href = "./favicon-white.png";
        titIm0.src = "./favicon-light.png";
        titIm1.src = "./favicon-light.png";
    } else {
        favLnk.href = "./favicon-black.png";
        titIm0.src = "./favicon-dark.png";
        titIm1.src = "./favicon-dark.png";
    }
};

updateTheme();

setInterval(updateTheme, 500);
