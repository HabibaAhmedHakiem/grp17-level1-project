# 1- Problem: Write a function divide_numbers(a, b) that takes two numbers a and b as input and handles the division operation.
# Catch the ZeroDivisionError if the second number b is zero and return a custom message.
# Sample Input: divide_numbers(10, 0)
# Expected Output: "Division by zero is not allowed!"

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed!"


output = divide_numbers(62, 0)

print(output)

