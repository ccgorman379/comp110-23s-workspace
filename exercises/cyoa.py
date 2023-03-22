"""EX06 - Choose Your Own Adventure Assignment - The Teller's Test."""

__author__ = "730556314"

from random import randint
points: int = 0
player: str = ""
path: int = 0
CRYSTAL_BALL: str = "\U0001F52E"


def greet() -> None:
    """Greeting and beginning of the game sequence."""
    global player
    print(f"Hello, traveller, and welcome to the Teller's Tent. {CRYSTAL_BALL}")
    print("My name is Elain, and I am a seer in this realm.")
    print("It seems you have sought me out to begin your own seer training, and I am more than happy to assist you in your quest for knowledge.")
    player = input("Before we begin, please, tell me your name traveller: ")
    print(f"Pleasure to meet you {player}!")
    print("Now, let's begin!")


def test(test_length: int) -> None:
    """Teller's Test, can be one or two numbers at a time."""
    global points
    another_round: bool = True
    while another_round is True:
        if test_length == 1:
            number: int = randint(1, 9)
            guess: int = input(f"Alright, {player}, I am thinking of one number from 1 to 9. What is your prediction?")
            if guess == number:
                print(f"Excellent, {player}! Your training is coming along quite nicely.")
                points += 1
            else: 
                print(f"Valiant effort, {player}, but your prediction was incorrect.")
            print(f"You have {points} correct guesses so far, {player}. Keep up the practice.")
            play_again_1: str = input(f"Would you like to try again, {player}? Yes or No?")
            if play_again_1 == "Yes":
                another_round is True
            else:
                another_round is False
        if test_length == 2:
            number_1: int = randint(1, 9)
            number_2: int = randint(1, 9)
            guess_1: int = input(f"Alright, {player}, I am thinking of two numbers from 1 to 9. What is your prediction for the first number?")
            guess_2: int = input("And your prediction for the second number?")
            if guess_1 == number_1 and guess_2 == number_2:
                print(f"Masterful work, {player}. You predicted both numbers correctly!")
                points += 2
            else:
                if guess_1 == number_1 or guess_2 == number_2:
                    print(f"Satisfactory job, {player}. You predicted one number correctly.")
                    points += 1
                else:
                    print(f"Good effort, {player}, but you did not predict either number correctly. Worry not, these things take decades of practice.")
            print(f"You have {points} correct guesses so far, {player}. Keep up the practice.")
            play_again_2: str = input(f"Would you like to try again, {player}? Yes or No?")
            if play_again_2 == "Yes":
                another_round is True
            else:
                another_round is False
         
                
def path_2(points: int) -> int:
    """Path 2 for info and extra points."""
    print(f"Kudos for seeking out more learning. A true seer at heart I see, {player}.")
    enter_path_2: str = input("Since you're here, are you ready for some insight into my test? Yes or No? ")
    while enter_path_2 != "Yes":
        enter_path_2: str = input(f"Please don't waste my time, {player}. Shall we proceed to the test information? Yes or No? ")
    print("My test will serve the purposes of a preliminary training for your seer abilities.")
    print("We will begin with a simple test: predicting numbers.")
    print("Though it may seem futile, a great seer must always begin with the basics of filtering out the noise of the world, focusing on a single task, simple as it may be.")
    print("I will think of a number from 1 to 9, and you shall simply make your prediction, providing it when promted.")
    print("Once you begin the test, you can choose to predict one or two numbers at a time.")
    print("Don't worry, traveller, I will keep track of how many correct guesses you get, letting you know along the way.")
    print(f"A good seer always seeks out all possible information, so just for seeking out knowledge, I will add 5 correct guesses to your total, {player}.")
    points += 5
    return points 


def main() -> None:
    """Main Game Function."""
    __name__ = "__main__"
    global player
    global points
    greet()
    print(f"Alright {player}, time to choose your path.")
    path: int = input("1. Leave the Teller's Tent \n2. Learn More About the Test \n3. Proceed to the Teller's Test ")
    while path == 2 or path == 3:
        print(f"You have {points} correct guesses so far, {player}. Keep up the practice.")
        if path == 2:
            points = path_2(points)
            print(f"You have {points} correct guesses so far, {player}. Keep up the practice.")
        if path == 3:
            test_length: int = input(f"How many numbers would you like to guess this time, {player}? 1 or 2?")
            test(test_length)
        path = input("1. Leave the Teller's Tent \n2. Learn More About the Test \n3. Proceed to the Teller's Test ")
    print(f"Hope you will come back to visit soon, {player}!")
    print(f"Your talents have greatly improved, and I am proud to say I have met you, a future seer. {CRYSTAL_BALL}")
    print(f"You have left the Teller's Tent with {points} correct guesses, a considerable feat.")
         

if __name__ == "__main__":
    main()