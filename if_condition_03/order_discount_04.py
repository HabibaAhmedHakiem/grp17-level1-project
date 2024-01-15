# program to get order discount
item_cost = 500
item_qty = 3
special_client = 1              # 1 ----> special    0----> not special

# processing ( program )
total_order_cost = item_cost * item_qty
if total_order_cost >= 1000:
    if special_client == 1:
        discount_pct = 20
    else:
        discount_pct = 10
else:
    discount_pct = 0

print('discount pct = ',discount_pct)
discount_value = discount_pct / 100 * total_order_cost
print('discount value =',discount_value)
total_order_cost = total_order_cost - discount_value
print('total order cost =',total_order_cost)
