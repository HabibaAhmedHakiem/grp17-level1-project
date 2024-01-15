# here we will show all basic operations on datetime
from datetime import datetime  # from module datetime import class datetime

print('.......get the current date and time.......')

today = datetime.now()
print(today)

print('.........get only the date or time or parts of them .......')

print(today.date())
print(today.date().day)
print(today.date().month)
print(today.date().year)
print(today.date().weekday())  # start from mon as 0 to sun as 6

print(today.time())
print(today.time().hour)
print(today.time().minute)
print(today.time().second)
print(today.time().microsecond)

print('...........Formatting date, time...we use strftime() function........')
print('.........convert date into string using strftime() function ...........')
print(today.strftime('%d-%m-%y'))     # d= day , m = month , y= year(last 2 digits) so as 24
print(today.strftime('%d-%m-%Y'))     # Y (capital) = as a 4 digit so 2024
print(today.strftime('%d-%m-%Y-%w'))  # w = weekday starts from sun as 0 to sat as 6
print(today.strftime('%d-%m-%Y-%W'))  # W = week no in the year
print(today.strftime('%d-%b-%Y-%w'))  #
print(today.strftime('%d-%B-%Y-%w'))  #
print(today.strftime('%a-%m-%Y-%w'))  #
print(today.strftime('%A-%m-%Y-%w'))  #
print(today.strftime('%H-%M-%S'))     #
print(today.strftime('%I-%M-%S'))     #
print(today.strftime('%I-%M-%S %p'))  # P= adds both Pm and Am


print('..............Create a custom date : 24-04-2023................')
print('...1st way : datetime object using constructor......')
# Custom_date = datetime(Year=2023, Month=4, Day=24)
custom_date = datetime(2023, 12, 25)
print(custom_date)

print('....2nd way - by converting a string to date...using strftime() function .... ')
date_style_string = '24-4-2023'
new_custom_date = datetime.strptime(date_style_string, '%d-%m-%Y')
print(new_custom_date)
print(new_custom_date.strftime('%d-%m-%Y'))

print('...............comparison..................')
if today.date() > custom_date.date():
    print('Today is newer than custom date')
elif today.date() < custom_date.date():
    print('Today is older than custom date')
else:
    print('2 dates are equal')

