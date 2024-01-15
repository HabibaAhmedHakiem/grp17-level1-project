# show string function
print('----------creat and print string -----------')
emp_name = 'yehiamomtaz'
print(emp_name)
print(type(emp_name))

print('--------------upper(), lowwer(), functions------------------')
upper_emp_name = emp_name.upper()   # all capital
lower_emp_name = emp_name.lower()   # all lower
print(emp_name.title())    # first letter capital
print(upper_emp_name)
print(lower_emp_name)
print(emp_name)

print('-------- isupper() , islower() , isalpha() function------- True, False ----------')
print(upper_emp_name.isupper())
print(upper_emp_name.islower())
print(lower_emp_name.isupper())
print(lower_emp_name.islower())
print(emp_name.isalpha())    # characters
print(emp_name.isalnum())    # characters or numbers
print(emp_name.isspace())
print(emp_name.isdigit())    # numbers

print('-------------endswith() function--------------')
file_path = 'c:/documents/egypt.pDf'
file_path = file_path.lower()
if file_path.endswith('pdf'):
    print('it is a book')
elif file_path.endswith('jpg') or file_path.endswith('bng'):
    print('it is an image')
else:
    print('unknown file type')

print('------------ startswith() function ------------')
emp_mobile = input('enter mobile? ')              # or emp_mobile = '+201061763348'
if emp_mobile.startswith('+20'):
    print('it is egyptian mobile')
elif emp_mobile.startswith('+966'):
    print('it is saudi mobile')
else:
    print('unknown')

