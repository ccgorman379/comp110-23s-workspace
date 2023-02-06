"""EX02 - One Shot Wordle Assignment - En Route to Wordle."""

__author__ = "730556314"
guess = input("What is your 6-letter guess? ")
SECRET = str("python")
while len(guess) != 6:
    guess = input("That was not 6 letters! Try again: ")
if (len(guess)) == 6:
    if guess == str(SECRET):
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")
#part 2
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
SECRET_indx: int = 0
guess_idx: int = 0
