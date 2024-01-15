# 3- Problem:
# Write a program that reads a user's first name, last name, and age,
# then formats and prints a welcome message using string formatting.

def welcome_message():
    first_name = input("Please write your first name: ")
    last_name = input("Please write your last name: ")
    age = input("Please write your age: ")

    welcome_mes = "Welcome, {} {}! You're {} years old.".format(first_name, last_name, age)
# or f"Welcome, {first_name} {last_name}! You're {age} years old"
    print(welcome_mes)


welcome_message()
