"""EX01 - Chardle Assignment - En Route to Wordle"""

_author_ = "730556314"
word = input("Enter a 5-character word: ")
if(len(word) != 5):
        print("Error: Word must contain 5 characters ")
        exit()

character = input("Enter a single character: ")
if(len(character) != 1):
        print("Error: Character must be a single character. ")
        exit()

print("Searching for " + character + " in " + word )
number_matching_characters:  int = 0

if(character == word[0]):
        print(character + " found at index 0")
        number_matching_characters = number_matching_characters + 1
if(character == word[1]):
        print(character + " found at index 1")
        number_matching_characters = number_matching_characters + 1
if(character == word[2]):
        print(character + " found at index 2")
        number_matching_characters = number_matching_characters + 1
if(character == word[3]):
        print(character + " found at index 3")
        number_matching_characters = number_matching_characters + 1
if(character == word[4]):
        print(character + " found at index 4")
        number_matching_characters = number_matching_characters + 1

if(number_matching_characters == 1):
        print(str(number_matching_characters) + " instance of " + character + " found in " + word)

if(number_matching_characters > 1):
        print(str(number_matching_characters) + " instances of " + character + " found in " + word)

if(number_matching_characters == 0):
        print("No instances of " + character + " found in " + word)
