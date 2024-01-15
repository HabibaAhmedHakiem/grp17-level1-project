# Solve password validation for rules

def valid_pass(pass_value):
    if len(pass_value) < 8:
        return False
    small_letter, capital_letter, special_letter, count_no = 0, 0, 0, 0

    for letter in pass_value:
        if letter.islower():
            small_letter = small_letter + 1
        elif letter.isupper():
            capital_letter = capital_letter + 1
        elif letter.isdigit():
            count_no = count_no + 1
        elif letter in '_@$':
            special_letter = special_letter + 1
    return all([small_letter > 0, capital_letter > 0, count_no > 0, special_letter > 0])

password = "ha_4545Aahmed"
result = valid_pass(password)

if result:
    print("Password is fine")
else:
    print("Password is not fine")