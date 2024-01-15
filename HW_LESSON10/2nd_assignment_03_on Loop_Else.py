# 3- Problem:
# Write a program that asks the user for a password and checks it against a predefined password.
# Use a while loop with an else block to print a message if the user fails to enter the correct password after three attempts.
def checking_password():
    right_password = "Habiba@2024"
    attempts = 2

    while attempts > 0:
        user_password = input('Please enter the password: ')

        if user_password == right_password:
            print('The password is correct')  # or print(f'The password is correct')
            break
        else:
            attempts = attempts - 1
            print(f'The password is incorrect. {attempts} attempts left.')
            # or print('The password is incorrect.', attempts, 'attempts left.')

    else:
        print('No more attempts left. Please try again later.')

checking_password()
