# program to validate password
"""
1. length > 8 letters
2. upper letters >= 1
3. digits >= 1
"""
password = 'E2e4e6e82e@'
count_upper , count_lower , count_digit , count_special = 0 , 0 , 0 , 0
if len(password) > 8:
    for letter in password:           # validate letters : loop over the string [ loop over letter by letter]
        if letter.isupper():
            count_upper = count_upper + 1
        elif letter.islower():
            count_lower = count_lower + 1
        elif letter.isdigit():
            count_digit = count_digit + 1
        elif not letter.isalnum():
            count_special = count_special + 1
    if count_upper > 0 and count_lower > 0 and count_digit > 0 and count_special > 0:
        print('password is valid')
    else:
        print(' password is not valid for letters validation ')
else:
    print('not valid password - len must be > 8 charecters')