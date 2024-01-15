# 3- Problem:
# Develop a program that reads an integer value from the user using input().
# Handle the ValueError if the entered input is not an integer then prompt the user until a valid integer is entered.

def get_right_integer():
    while True:
        try:
            users_input = input("Please Enter an integer: ")
            value = int(users_input)
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")


right_integer = get_right_integer()

print("Your integer is:", right_integer)
