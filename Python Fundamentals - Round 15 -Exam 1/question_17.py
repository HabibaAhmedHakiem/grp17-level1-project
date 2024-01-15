# loop over all keys and raise the prices 10% Print sum of all the values after raise 10%  Add vat 14% to the total and print the net value

shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
total_sum = 0

for key, value in shopping_cart_dict.items():
    shopping_cart_dict[key] = value + value * 10/100
    total_sum = total_sum + shopping_cart_dict[key]

print('After 10% raise: ', shopping_cart_dict)
print('Total sum: ', total_sum)


sum_net_value = total_sum + total_sum * 14/100
print('Net value = ', sum_net_value)

