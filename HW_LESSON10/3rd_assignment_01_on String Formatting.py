# 1- Problem:
# Create a function format_currency(amount) that takes a floating-point number representing an amount
# and returns a string formatted as currency (with a dollar sign and two decimal places).
# 7000 > 7,000.00$

def format_currency(amount):
    return f'{amount:,.02f}$'

amount = 7000.0
formatted_amount = format_currency(amount)

print(f'The Amount: {amount}')
# or print('The Amount:', amount)
print(f'Amount in Currency: {formatted_amount}')
# or print('Amount in Currency:', formatted_amount)
