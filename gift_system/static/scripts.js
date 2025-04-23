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

    function changeSlide(n) {
        const slides = document.getElementsByClassName("slide");

        slides[slideIndex - 1].style.display = "none";
        slideIndex += n;

        if (slideIndex > slides.length) { slideIndex = 1; }
        if (slideIndex < 1) { slideIndex = slides.length; }

        slides[slideIndex - 1].style.display = "block";
    }

    showSlides();

    function filterGifts() {
        var ageGroup = document.getElementById("ageGroup").value;
        var interest = document.getElementById("interest").value;
        var giftCards = document.querySelectorAll('.gift-card');

        giftCards.forEach(function(card) {
            var cardAge = card.getAttribute('data-age');
            var cardInterest = card.getAttribute('data-interest');

            // Check if the card matches the selected filters
            if ((ageGroup === "All" || cardAge === ageGroup) && (interest === "All" || cardInterest === interest)) {
                card.style.display = "block"; // Show the gift card
            } else {
                card.style.display = "none"; // Hide the gift card
            }
        });
    }
});
