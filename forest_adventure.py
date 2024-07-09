def start_game():
    print("******************************")
    print("      The Forest Adventure")
    print("******************************")
    print("Welcome to the adventure game!")
    print("You wake up in a forest and can go in three directions: north, south, or west.")
    choice = input("Which way do you go? (north/south/west): ").strip().lower()

    if choice == "north":
        north()
    elif choice == "south":
        south()
    elif choice == "west":
        west()
    else:
        print("Invalid choice. Please try again!")
        start_game()

def north():
    print("You encounter a wolf.")
    print("1. Fight the wolf")
    print("2. Run away")
    choice = input("What do you do? (1/2): ").strip()
    
    if choice == "1":
        print("The wolf was too strong. Unfortunately, you lose the game.")
        restart_game()
    elif choice == "2":
        print("You successfully escaped. You return to the starting point.")
        start_game()
    else:
        print("Invalid choice. Please try again!")
        north()

def south():
    print("You come across an abandoned house.")
    print("1. Enter the house")
    print("2. Move on")
    choice = input("What do you do? (1/2): ").strip()

    if choice == "1":
        print("You find nothing interesting in the house. You return to the starting point.")
        start_game()
    elif choice == "2":
        print("You move on but find nothing interesting. You return to the starting point.")
        start_game()
    else:
        print("Invalid choice. Please try again!")
        south()

def west():
    print("You find the exit! Congratulations, you win!")
    restart_game()

def restart_game():
    choice = input("Do you want to play again? (yes/no): ").strip().lower()
    if choice == "yes":
        start_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    start_game()
