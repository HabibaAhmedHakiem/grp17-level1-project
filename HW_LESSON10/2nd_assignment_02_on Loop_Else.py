# 2- Problem:
# Develop a program that iterates through a string and checks for the presence of a specific character.
# Use a for loop with an else block to print a message if the character is not found.

def check_character(input_str, specific_character):
    for character in input_str:
        if character == specific_character:
            print(f"Character '{specific_character}' is found in the str ")
            break    # or print('character', specific_character, 'is not found in string')
    else:
        print(f"Character '{specific_character}' isn't found in the str")
    # or print('character', specific_character, " isn't found in the str")


input_str = 'My name is Habiba Ahmed@'
specific_char = "!"

check_character(input_str, specific_char)
