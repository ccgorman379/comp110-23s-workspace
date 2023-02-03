"""Asks user for a number, goes until they get it right"""

SECRET = int(4)  #not changing means it's in all caps
guess: int = int(input("Guess a number! "))
playing: bool = True
number_of_guesses: int = 1

while playing:   #could also do "while playing and number_of_guesses < 3: " instead of lines 9 and 10
    if number_of_guesses == 3:
       playing = False
    if guess == SECRET:
        print("Yay! You got it right.")
        playing = False
    else:
        print("Wrong number. :(")
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd. The answer is even.")
        if guess > SECRET:
            print("Your guess is too high! ")
        else: #guess < secret
            print("Your guess is too low. ")
        guess = int(input("Make another guess! "))
    number_of_guesses = number_of_guesses + 1 
    print("Number of guesses " + str(number_of_guesses))