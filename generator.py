import random 
import string

def generate_password(min_length, num = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    if num:
        characters += digits
    if special_characters:
        characters += special
    password = ""
    has_number = False
    has_special = False
    while len(password) < min_length or has_number != num or has_special != special_characters:
        char = random.choice(characters)
        if char in digits:
            has_number = True
        elif char in special:
            has_special = True
        password += char
    return password