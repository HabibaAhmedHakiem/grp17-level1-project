# 5- Problem:
# Implement a function format_percentage(decimal) that takes a decimal number ( 50.25716 ) and
# returns a string representation of the percentage with two decimal places (e.g., "50.25%").

def format_percentage(decimal):
    formatted_percentage = "{:.02%}".format(decimal)

    return formatted_percentage


decimal_number = 50.25716
formatted_percentage = format_percentage(decimal_number)

print(f"The Original Decimal Number: {decimal_number}")
print(f"Formatted Percentage: {formatted_percentage}")
