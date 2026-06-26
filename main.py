from ui import show_menu, show_rules
from game import start_game

while True:

    choice = show_menu()

    if choice == "1":
        start_game()

    elif choice == "2":
        show_rules()

    elif choice == "3":
        break

    else:
        print("Invalid Choice")

    input("\nPress Enter...")