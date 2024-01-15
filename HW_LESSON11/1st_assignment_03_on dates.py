# 3- Problem:
# program checks if a specific date falls between two provided dates.
# Input :
# start_date = datetime(2023, 1, 1)
# end_date = datetime(2023, 12, 31)
# given_date = datetime(2023, 6, 15)
#
# dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
# Output :
# The date is in range

from datetime import datetime

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
given_date = datetime(2023, 6, 15)

if end_date >= given_date >= start_date:
    print("The date is in range")
else:
    print("The date is not in range")

