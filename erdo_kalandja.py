def start_game():
    print("Üdvözöllek a kalandjátékban!")
    print("Egy erdőben ébredsz, és három irányba mehetsz: észak, dél vagy nyugat.")
    choice = input("Merre mész? (észak/dél/nyugat): ").strip().lower()

    if choice == "észak":
        north()
    elif choice == "dél":
        south()
    elif choice == "nyugat":
        west()
    else:
        print("Nem érvényes választás. Próbáld újra!")
        start_game()

def north():
    print("Egy farkassal találkozol, és sajnos elveszted a játékot.")
    restart_game()

def south():
    print("Egy elhagyatott házra bukkansz, és semmi érdekeset nem találsz.")
    print("Visszamész a kiindulópontra.")
    start_game()

def west():
    print("Megtalálod a kijáratot! Gratulálok, nyertél!")
    restart_game()

def restart_game():
    choice = input("Szeretnéd újra játszani? (igen/nem): ").strip().lower()
    if choice == "igen":
        start_game()
    else:
        print("Köszönöm, hogy játszottál!")

if __name__ == "__main__":
    start_game()