document.addEventListener("DOMContentLoaded", () => {
    const dropdowns = document.querySelectorAll("nav div");

    dropdowns.forEach(dropdown => {
        dropdown.addEventListener("mouseenter", () => {
            dropdown.querySelector("ul").style.display = "block";
        });
        dropdown.addEventListener("mouseleave", () => {
            dropdown.querySelector("ul").style.display = "none";
        });
    });

    let slideIndex = 0;

    function showSlides() {
        const slides = document.getElementsByClassName("slide");

        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }

        slideIndex++;
        if (slideIndex > slides.length) { slideIndex = 1; }

        slides[slideIndex - 1].style.display = "block";
        setTimeout(showSlides, 3000); // Change image every 3 seconds
    }

    showSlides();

    const element = document.getElementById('yourElementId');
    console.log(document.getElementById('yourElementId'));
    if (element) {
        element.addEventListener('click', () => {
            console.log('Element clicked!');
        });
    } else {
        console.error('Element with ID "yourElementId" not found.');
    }
});
