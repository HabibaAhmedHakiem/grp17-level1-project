# 5- Problem:
# Check if all dates in a list are in the same month:
# Sample Input:
# dates_list = [
#     datetime(2023, 12, 31),
#     datetime(2023, 12, 15),
#     datetime(2023, 12, 15),
#     datetime(2023, 12, 1)
# ]
# Output :
# All dates are in the same month : 12

from datetime import datetime

dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 12, 15),
    datetime(2023, 12, 15),
    datetime(2023, 12, 1)
]

example_month = dates_list[0].month

for item in dates_list:
    if item.month != example_month:
        print(f'All dates are not in the same month')
        break
else:
    print(f'All dates are in the same month : {example_month}')

