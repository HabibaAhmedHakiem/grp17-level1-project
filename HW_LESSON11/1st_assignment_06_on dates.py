# 6- Problem:
# Create a list of dates within a date range included:
# Sample Input:
# start_range = datetime(2023, 1, 1)
# end_range = datetime(2023, 1, 10)
# Output :
# dates_list = [datetime(2023, 1, 1) ,,…,…,, datetime(2023,1,10)]

from datetime import datetime
from dateutil import relativedelta

new_list = []
start_range = datetime(2023, 1, 1)
end_range = datetime(2023, 1, 10)

present_range = start_range

while present_range <= end_range:
    new_list.append(present_range.date())
    present_range = present_range + relativedelta.relativedelta(days = 1)

print(new_list)

