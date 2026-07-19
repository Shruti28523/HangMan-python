const playButton = document.getElementById("play-btn");
const backButton = document.getElementById("back-btn");
const exitButton = document.getElementById("exit-btn");

const mainMenu = document.getElementById("main-menu");
const categoryMenu = document.getElementById("category-menu");
const gameScreen = document.getElementById("game-screen");

const categoryCards = document.querySelectorAll(".category-card");

const gameTitle = document.getElementById("game-title");
const wordDiv = document.getElementById("word");

// Game Variables
let selectedWord = "";
let guessedLetters = [];
let wrongLetters = [];
let lives = 6;


function displayWord() {

    let display = "";

    for (let letter of selectedWord) {

        if (guessedLetters.includes(letter)) {
            display += letter + " ";
        } else {
            display += "_ ";
        }

    }

    wordDiv.textContent = display;

}

function updateLives() {

    let hearts = "";

    for (let i = 0; i < lives; i++) {
        hearts += "❤️ ";
    }

    for (let i = lives; i < 6; i++) {
        hearts += "🖤 ";
    }

    document.getElementById("lives").textContent = hearts;

}


function updateWrongLetters() {

    document.getElementById("wrong-letters").textContent =
        "Wrong Letters: " + wrongLetters.join(" ");

}


document.addEventListener("keydown", function (event) {

    const letter = event.key.toUpperCase();

    if (!/^[A-Z]$/.test(letter)) return;

    if (guessedLetters.includes(letter) || wrongLetters.includes(letter)) return;

    if (selectedWord.includes(letter)) {

        guessedLetters.push(letter);

        displayWord();

        // WIN CHECK
        let won = true;

        for (let ch of selectedWord) {

            if (!guessedLetters.includes(ch)) {
                won = false;
                break;
            }

        }

        if (won) {

            setTimeout(() => {

                alert("🎉 You Win!");

            }, 100);

        }

    }

    else {

        wrongLetters.push(letter);

        lives--;

        updateWrongLetters();

        updateLives();

        if (lives === 0) {

            setTimeout(() => {

                alert("💀 Game Over!\n\nThe word was " + selectedWord);

            }, 100);

        }

    }

});

// ---------------- PLAY ----------------

playButton.addEventListener("click", function () {

    mainMenu.classList.add("fade-out");

    setTimeout(function () {

        mainMenu.style.display = "none";
        categoryMenu.style.display = "block";

        categoryMenu.classList.add("fade-in");

    }, 400);

});


// ---------------- BACK ----------------

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


// ---------------- CATEGORY ----------------

categoryCards.forEach(card => {

    card.addEventListener("click", async function () {

        const category = card.dataset.category;

        gameTitle.textContent = category;

        // Ask Flask for a random word
        const response = await fetch(`/get-word/${category}`);

        const data = await response.json();

        selectedWord = data.word;
        guessedLetters = [];
        wrongLetters = [];
        lives = 6;

        updateLives();
        updateWrongLetters();

        displayWord();

       
      
        categoryMenu.classList.remove("fade-in");
        categoryMenu.classList.add("fade-out");

        setTimeout(function () {

            categoryMenu.style.display = "none";

            gameScreen.style.display = "block";

            gameScreen.classList.add("fade-in");

        }, 400);

    });

});


// ---------------- EXIT ----------------

exitButton.addEventListener("click", function () {

    gameScreen.classList.remove("fade-in");
    gameScreen.classList.add("fade-out");

    setTimeout(function () {

        gameScreen.style.display = "none";

        categoryMenu.style.display = "block";

        categoryMenu.classList.remove("fade-out");
        categoryMenu.classList.add("fade-in");

    }, 400);

});


// ---------------- RESET ANIMATION ----------------

document.querySelectorAll(".menu").forEach(menu => {

    menu.addEventListener("animationend", function () {

        menu.classList.remove("fade-in");

    });

});