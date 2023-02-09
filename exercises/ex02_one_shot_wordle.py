"""EX02 - One Shot Wordle Assignment - En Route to Wordle."""

__author__ = "730556314"
guess = input("What is your 6-letter guess? ")
SECRET = str("python")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess_idx: int = 0
result: str = ""
while len(guess) != len(SECRET):
    guess = input("That was not " + str(len(SECRET)) + " letters! Try again: ")
if (len(guess)) == len(SECRET):
    while guess_idx < len(SECRET):
        if guess[guess_idx] == SECRET[guess_idx]:
            result = result + GREEN_BOX
        else:
            alt_location = False
            alt_idx: int = 0
            while not (alt_location is True) and (alt_idx < len(SECRET)):
                if SECRET[alt_idx] == guess[guess_idx]:
                    alt_location = True
                else:
                    alt_idx = alt_idx + 1
            if alt_location is True:
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
        guess_idx = guess_idx + 1
    print(result)
if guess == SECRET:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")