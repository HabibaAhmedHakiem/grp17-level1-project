# 4- Problem:
# Count occurrences of a specific date in a list:
# Sample Input:
# dates_list = [
#     datetime(2023, 12, 31),
#     datetime(2023, 8, 15),
#     datetime(2023, 8, 15),
#     datetime(2023, 5, 1)
# ]
# given_date = datetime(2023, 8, 15)
# Output :
# 2023-08-15 occurs 2 times

from datetime import datetime

dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 8, 15),
    datetime(2023, 8, 15),
    datetime(2023, 5, 1)
]
given_date = datetime(2023, 8, 15)

count_occurrence = 0

for date in dates_list:
    if date == given_date:
        count_occurrence = count_occurrence + 1

print(f"{given_date.date()} occurs {count_occurrence} times")

