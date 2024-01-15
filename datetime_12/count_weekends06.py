# program to count friday or saturday in a specific month
from datetime import datetime
from dateutil import relativedelta

# input
year = 2023
month = 11

# coding
custom_date = datetime(year, month, 1)
end_date = custom_date + relativedelta.relativedelta(months=1)
weekend_counters = 0
while custom_date < end_date:
    if custom_date.date().weekday() in [4, 5]:    # monday = 0 it's like an index so tuesday = 1, wednesday = 2,...
        weekend_counters = weekend_counters + 1

    custom_date = custom_date + relativedelta.relativedelta(days=1)

print(f'weekend counter  Fri or Sat is {weekend_counters}')