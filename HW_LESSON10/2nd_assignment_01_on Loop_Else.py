# 1- Problem:
# Create a program that iterates through a list of numbers and prints all even numbers.
# Implement an else block to display a message if no even numbers are found in the list.

def print_all_even_numbers(numbers):
    even_num_found = False

    for num in numbers:
        if num % 2 == 0:
            print('the even number found is:', num)  # or f'the even number found is: {num}'
            even_num_found = True

    if not even_num_found:
        print('No even number is found in the list ')  # or f' no even number is found in the list '


num_list = [3, 4, 6, 2, 1, 9]

print('check for the even numbers:')  # or f"check for the even numbers:"
print_all_even_numbers(num_list)
