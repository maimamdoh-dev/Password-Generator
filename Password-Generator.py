import random
import string

def generate_password(min_Lenght, numbers=True , speical_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    speical= string.punctuation

    characters = letters
    if numbers :
        characters += digits
    if speical_characters:
        characters += speical
    
    password = ""
    meet_criteria = False
    has_number = False
    has_special = False


    while not meet_criteria or len(password) < min_Lenght:
        new_character = random.choice(characters)
        password += new_character

        if new_character in digits:
            has_number = True
        elif new_character in speical:
            has_special = True
        
        meet_criteria = True 
        if numbers:
            meet_criteria = has_number
        if speical_characters:
            meet_criteria = meet_criteria and has_special
    return password


min_length = int(input("Enter the minimum length: "))

has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"

has_speical = input("Do you want to have speical characters (y/n)? ").lower() == "y"

password = generate_password(min_length , has_number , has_speical)
print("The Generated password is: " , password)