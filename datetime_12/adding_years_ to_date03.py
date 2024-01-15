# program to add , subtract 2 years, 5 month, 7 days to a date
from datetime import datetime
from dateutil import relativedelta

today = datetime.now()

# new_date = today + 5  this gives eror : should use relativedelta
new_date = today + relativedelta.relativedelta(years=2, months=5, days=7)
print(new_date)


