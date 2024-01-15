# 4- Problem:
# Write a function format_phone_number(number) that takes an unformatted phone number (as a string) and
# returns it in a formatted form
# 11234567890 > +1 (123) 456-7890

def format_phone_number(number):
    original_number = ''.join(char for char in number if char.isdigit())
    formatted_number = "+1 ({}) {}-{}".format(original_number[:3], original_number[3:6], original_number[6:])

    return formatted_number


unformatted_number = "11234567890"
formatted_number = format_phone_number(unformatted_number)

print(f"The Original Number: {unformatted_number}")
print(f"Formatted Number: {formatted_number}")


