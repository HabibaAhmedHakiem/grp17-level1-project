# program to show the nearest sunday
import calendar
from datetime import datetime
from dateutil import relativedelta

today =datetime.now()

print('.......the nearest sunday from today...........')
nearest_sunday = today + relativedelta.relativedelta(weekday=calendar.SUNDAY)   # jumps to the nears sunday
print(nearest_sunday)

print('.......the nearest second sunday from today............')
nearest_2nd_sunday = today + relativedelta.relativedelta(weekday=calendar.SUNDAY, weeks=1)  # jumps to the nears 2nd sun
print(nearest_2nd_sunday)


