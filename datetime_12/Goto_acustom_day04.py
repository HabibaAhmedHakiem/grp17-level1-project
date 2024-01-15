# program to go to a specific day in a date
from datetime import datetime
from dateutil import relativedelta

today =datetime.now()  # 25-12-2023

print('..........Get to the first day in a month...........')
first_day = today + relativedelta.relativedelta(day = 1)  # replace 25-12-2023 to 1-12-2023
print(first_day)

print('...........get to the last day in this month..............')
last_day = today + relativedelta.relativedelta(day = 31)  # replace 25-12-2023 to 31-12-2023
print(last_day)
