import random
from rich.console import Console
from rich.panel import Panel

console = Console()

# ----------------------------
# WORDS
# ----------------------------
words = [
    "python", "banana", "computer", "guitar", "elephant",
    "astronaut", "volcano", "library", "penguin",
    "galaxy", "mountain", "diamond", "football",
    "keyboard", "umbrella", "treasure", "chocolate"
]

# ----------------------------
# HANGMAN STAGES
# ----------------------------
hangman = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]


def play_game():

    secret_word = random.choice(words)
    guessed_letters = []
    display = ["_"] * len(secret_word)
    lives = 6

    while lives > 0 and "_" in display:

        console.clear()

        console.print(
            Panel.fit(
                "[bold cyan]🎮 HANGMAN[/bold cyan]",
                subtitle="Guess the word!"
            )
        )

        console.print(hangman[6 - lives])

        console.print(f"\nWord: {' '.join(display)}")
        console.print(f"\nLives: ❤️ {lives}")
        console.print(f"Guessed Letters: {', '.join(guessed_letters)}")

        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            console.print("\n[red]Please enter ONE alphabet letter.[/red]")
            input("\nPress Enter...")
            continue

        if guess in guessed_letters:
            console.print("\n[yellow]You already guessed that letter![/yellow]")
            input("\nPress Enter...")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display[i] = guess

        else:
            lives -= 1

    console.clear()

    if "_" not in display:
        console.print(
            Panel.fit(
                "[bold green]🎉 YOU WON! 🎉[/bold green]"
            )
        )
    else:
        console.print(hangman[6])
        console.print(
            Panel.fit(
                "[bold red]GAME OVER[/bold red]"
            )
        )

    console.print(f"\nThe word was: [bold]{secret_word}[/bold]\n")


# ----------------------------
# MAIN MENU
# ----------------------------

while True:

    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]🎮 HANGMAN[/bold cyan]",
            subtitle="Version 1.0"
        )
    )

    console.print("\n[green]1.[/green] Start Game")
    console.print("[red]2.[/red] Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        play_game()
        input("\nPress Enter to return to menu...")

    elif choice == "2":
        console.print("\nGoodbye! 👋")
        break

    else:
        console.print("\nInvalid choice.")
        input("\nPress Enter...")