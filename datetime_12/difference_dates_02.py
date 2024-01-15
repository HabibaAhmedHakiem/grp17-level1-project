# get the difference between 2 dates in days as a total
from datetime import datetime
from dateutil import relativedelta

today = datetime.now()
custom_date = datetime(2005,2,8)

difference_in_days = today - custom_date
print(difference_in_days)
print(difference_in_days.days)

print('............. using relative delta class; to get difference .............')
difference_parts = relativedelta.relativedelta(today, custom_date)
print(difference_parts)
print(f'years ={difference_parts.year}, months = {difference_parts.month}, days = {difference_parts.days}')



