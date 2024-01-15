# 1- Problem:
# Find the earliest (oldest) date from a list of dates
# Input :
# dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
# Output :
# 2023-05-01

from datetime import datetime

dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
oldest_date = dates_list[1]

for item in dates_list:
    if item < oldest_date:
        oldest_date = item

print(oldest_date.date())