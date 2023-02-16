"""Practice Writing Functions"""

def mimic(my_words:str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

print(mimic("Hello!"))

my_words: str = "Hello!"



def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return("Index too high")
    else:
        return my_words[letter_idx]