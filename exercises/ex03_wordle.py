"""EX03 - Wordle Assignment - The Final Destination"""

__author__ = "730556314"
def contains_char(search: str, char: str) -> bool:
    """Given one long string and a single character, returns if single character is in long string"""
    assert len(char) == 1
    alt_location = False
    search_idx: int = 0
    while not (alt_location is True) and search_idx < len(search):
        if search[search_idx] == char:
            alt_location = True
        else:
            search_idx = search_idx + 1
    if alt_location is True:
        return True
    else:
        return False

def emojified(guess: str, SECRET: str) -> str:
    """Given two strings of equal length, returns color codified string"""
    assert len(guess) == len(SECRET)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    guess_idx: int = 0
    result: str = ""
    while guess_idx < len(SECRET):
        if guess[guess_idx] == SECRET[guess_idx]:
            result = result + GREEN_BOX
        else:
            if contains_char(SECRET, guess[guess_idx]) is True:
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
        guess_idx = guess_idx + 1
    return result

def input_guess(expected_length: int) -> str:
    """Given expected guess length, prompts for a guess of the designated length"""
    guess = input("Enter a " + str(expected_length) + " character word: ")
    while len(guess) != expected_length:
        guess = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    if len(guess) == expected_length:
        return guess
    else:
        return guess

def main() -> None:
    """The entrypoint of the program and main game loop"""
    turn_number: int = 1
    SECRET: str = "codes"
    guess_idx: int = 0
    guess: str = ""
    while turn_number <= 6 and guess != SECRET:
        print("=== Turn " + str(turn_number) + "/6 ===")
        guess = input_guess(len(SECRET))
        print(emojified(guess, SECRET))
        turn_number = turn_number + 1
    if guess == SECRET:
        return print("You won in " + str(turn_number - 1) + "/6 turns!")
    else:
        return print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()