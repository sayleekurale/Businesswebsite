// Scroll Animation for Sustainability Section
document.addEventListener("scroll", function () {
    const containers = document.querySelectorAll(".sustainability-container");
    containers.forEach(container => {
        const position = container.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        if (position < windowHeight - 100) {
            container.classList.add("show");
        }
    });
});
// Scroll Animation for Quote Section

document.addEventListener("scroll", function () {
    const quoteContent = document.querySelector(".quote-content");
    const position = quoteContent.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;

    if (position < windowHeight - 100) {
        quoteContent.classList.add("show");
    }
});
// JavaScript for hero image carousel
const heroImages = [
    "{{ url_for('static', filename='images/sustainbg.jpeg') }}",
    "{{ url_for('static', filename='images/sustainbg1.jpeg') }}", // Replace with your second image
    "{{ url_for('static', filename='images/sustainbg2.jpeg') }}"  // Replace with your third image
];

let currentHeroIndex = 0;

function changeImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length; // Cycle through images
    console.log("Current Image Index: ", currentImageIndex);
    console.log("Current Image URL: ", images[currentImageIndex]);
    mainImage.style.opacity = 0; // Fade out
    setTimeout(() => {
        mainImage.src = images[currentImageIndex]; // Change the image source
        mainImage.style.opacity = 1; // Fade in
    }, 500); // Match with CSS transition duration
}


// Automatic image change every 30 seconds
setInterval(changeImage, 30000);

// JavaScript for gallery images
document.querySelectorAll('.gallery-item').forEach(item => {
    let index = 0;
    const hiddenImages = item.querySelector('.hidden-images').children;

    // Hide all hidden images initially
    for (let i = 0; i < hiddenImages.length; i++) {
        if (i !== index) {
            hiddenImages[i].style.display = 'none';
        }
    }

    setInterval(() => {
        hiddenImages[index].style.display = 'none'; // Hide current
        index = (index + 1) % hiddenImages.length; // Move to next
        hiddenImages[index].style.display = 'block'; // Show next
    }, 1000); // Change every 3 seconds
});


