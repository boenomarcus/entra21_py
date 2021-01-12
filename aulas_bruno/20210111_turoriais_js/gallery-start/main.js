// Connect JS to DOM objects
const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');
const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

// Looping through images
for (let i = 1; i <= 5; i++) {
    const newImage = document.createElement('img');
    newImage.setAttribute('src', 'images/pic' + i + '.jpg');
    thumbBar.appendChild(newImage);
    newImage.onclick = function(e) {
        displayedImage.src = e.target.src;
    }
}

// Wiring up the Darken/Lighten button
function changeOpacity_ImgDisplay() {
    
    // Get current class
    let test = btn.getAttribute('class')
    
    //  Update opacity
    if (test == "dark") {
        // Set opacity to light
        btn.setAttribute('class', 'light');
        btn.textContent = "Lighten";
        overlay.style.backgroundColor = "rgba(0,0,0,0.5)";
    } else {
        // Set opacity to dark
        btn.setAttribute('class', 'dark');
        btn.textContent = "Darken";
        overlay.style.backgroundColor = "rgba(0,0,0,0)";
    }
}

// Add Event listener
btn.addEventListener('click', changeOpacity_ImgDisplay)
