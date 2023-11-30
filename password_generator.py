from sys import exit

import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
           has_number = True
        elif new_char in special:
           has_special = True

        #update the meets_criteria variable
        meets_criteria = True
        #if we can turn into the value of meets_criteria variable to false, then it doesn't meets the given criteria :)

        if numbers:
            meets_criteria = has_number
        #if we don't have a number but we're supposed to include a number, we don't meet the criteria. That's why we incuded this situation with  an and operator:
        if special_characters:
            meets_criteria = has_special and meets_criteria

    return pwd
        
min_length = int(input("enter the minimum length: "))
has_number = input("do you want to have numbers?     (y/n)").lower() == "y"
has_special = input("do you want to have special characters?    (y/n)").lower == "y"
pwd = generate_password(min_length, has_number, has_special)
print("the generated password is: ",pwd)

exit()
