from rich.console import Console
from rich.panel import Panel

console = Console()


def show_menu():

    console.clear()

    console.print(
        Panel(
            "[bold cyan]🎮 HANGMAN[/bold cyan]",
            subtitle="Version 2.0"
        )
    )

    console.print("[green]1.[/green] Play")
    console.print("[yellow]2.[/yellow] Rules")
    console.print("[red]3.[/red] Exit")

    choice = input("\nChoose an option: ")

    return choice
    console.print(f"[bold cyan]{load_logo()}[/bold cyan]")

def show_rules():

    console.clear()

    console.print("[bold yellow]📖 HOW TO PLAY[/bold yellow]\n")

    console.print("• Guess one letter at a time.")
    console.print("• Every wrong guess loses one life.")
    console.print("• Guess the entire word before the hangman is complete.")
    console.print("• Have fun!\n")

    input("Press Enter to return...")

def load_logo():
    with open("assets/logo.txt", "r", encoding="utf-8") as file:
        return file.read()