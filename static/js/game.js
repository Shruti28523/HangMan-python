const playButton = document.getElementById("play-btn");
const backButton = document.getElementById("back-btn");

const mainMenu = document.getElementById("main-menu");
const categoryMenu = document.getElementById("category-menu");

playButton.addEventListener("click", function () {

    mainMenu.classList.add("fade-out");

    setTimeout(function () {

        mainMenu.style.display = "none";

        categoryMenu.style.display = "block";

        categoryMenu.classList.add("fade-in");

    }, 400);

});

backButton.addEventListener("click", function () {

    categoryMenu.classList.remove("fade-in");
    categoryMenu.classList.add("fade-out");

    setTimeout(function () {

        categoryMenu.style.display = "none";

        mainMenu.style.display = "block";

        mainMenu.classList.remove("fade-out");
        mainMenu.classList.add("fade-in");

    }, 400);

});

document.querySelectorAll(".menu").forEach(menu => {

    menu.addEventListener("animationend", function () {

        menu.classList.remove("fade-in");

    });

});