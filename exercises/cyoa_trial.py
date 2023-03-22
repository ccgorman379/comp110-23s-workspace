"""EX06 - Choose Your Own Adventure Assignment - Which Archeron Sister Are You?"""

__author__ = "730556314"

points: int = 0
player: str = ""


def greet() -> None:
    """Greeting and beginning of the game sequence"""
    print("Hello, human, and welcome to the faerie realm of Pyrthian!")
    print("My name is Feyre Archeron, High Lady of the Night Court, and I have the pleasure of assisting you today.")
    print("I heard you wanted to see which of the famed Acheron sisters you are most like, so we shall do just that!")
    global player
    player: str = input("Before we begin, please, tell me your name: ")
    print(f"Pleasure to meet you {player}!")
    print("Now, let's begin!")

def quiz() -> None:
    """Option 2 """







def main() -> None:
    __name__ = "__main__"
    global points
    greet()
    print(f"Alright {player}, time to choose your path.")
    path: int = input(f"1. Leave Prythian Now\n2. Learn More About Pyrithian\n3. Proceed to the Archeron Sister Quiz")
    if path == 1:
        print(f"Hope you will come back to visit soon, {player}!")
        print(points)
        quit()
    if path == 2:




if __name__ == "__main__":
    main()