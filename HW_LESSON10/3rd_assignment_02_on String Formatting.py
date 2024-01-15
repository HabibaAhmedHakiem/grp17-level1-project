# 2- Problem:
# Implement a function format_order(item, price, quantity) that takes the name of an item,
# its price, and quantity as arguments, then returns a formatted string representing an order.
# The order contains rice, price = 70.00$, quantity = 2 plates

def format_order(item, price, quantity):
    formatted_price = format_currency(price)
    return f'The order contains {item}, price = {formatted_price}, quantity = {quantity}.'
# or print('The order contains', item, ', price =', formatted_price,', quantity = ', quantity )


def format_currency(amount):
    return f'{amount:,.02f}$'


item_name = 'rice'
item_price = 70.00
item_quantity = 2

order_info = format_order(item_name, item_price, item_quantity)
print(order_info)
