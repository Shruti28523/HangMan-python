from rich.console import Console
from words import load_words

console = Console()
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


def choose_category():

    console.clear()

    console.print("[bold cyan]Choose a Category[/bold cyan]\n")

    console.print("1. Animals")
    console.print("2. Countries")
    console.print("3. Food")
    console.print("4. Movies")
    console.print("5. Programming")
    console.print("6. Random")

    choice = input("\nChoose a category: ")

    return choice


def get_category(choice):

    categories = {
        "1": "animals",
        "2": "countries",
        "3": "food",
        "4": "movies",
        "5": "programming"
    }

    return categories.get(choice)


def start_game():

    choice = choose_category()

    category = get_category(choice)

    secret_word = load_words(category)

    display = []

    for letter in secret_word:
      display.append("_")
    lives = 6
    wrong_letters = []
    guessed_letters = []

    while "_" in display and lives > 0:

     console.clear()

     console.rule("[bold cyan]🎮 HANGMAN[/bold cyan]")
     console.print(f"[bold yellow]📂 Category:[/bold yellow] {category.title()}")
     console.print(hangman[6 - lives])
     console.print(f"[bold green]Word:[/bold green] {' '.join(display)}")

     console.print(f"[bold red]❤️ Lives:[/bold red] {lives}")

     console.print(f"[bold magenta]❌ Wrong:[/bold magenta] {' '.join(wrong_letters)}")

     console.print(f"[bold blue]📝 Guessed:[/bold blue] {' '.join(guessed_letters)}")

     console.rule() 
    

     guess = input("\nGuess a letter: ").lower().strip()

     if len(guess) != 1 or not guess.isalpha():
         console.print("\n[red]Please enter ONE letter only![/red]")
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
        wrong_letters.append(guess)
    
    if lives == 0:
      console.print("\n💀 Game Over! You ran out of lives.")
    else:
      console.print("\n🎉 Congratulations! You guessed the word!")
    console.print(f"The word was: {secret_word}")
    input("\nPress Enter...")