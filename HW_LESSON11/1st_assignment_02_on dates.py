# Check if a specific date exists in a list of dates
# Sample Input:
# given_date = datetime(2023, 8, 15)
# dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
# Expected Output: 2023-08-15 is found in the list at index 1
from datetime import datetime

given_date = datetime(2023, 8, 15)
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]

try:
    index = dates_list.index(given_date)
    print(f"{given_date.date()} is found in the list at index {index}")
except ValueError:
    print(f"{given_date.date()} is not found in the list.")


