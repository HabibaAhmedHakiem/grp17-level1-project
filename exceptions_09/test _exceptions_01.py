# to show how to handle exceptions

try:
    first_number = int(input('please enter first number: '))
    second_number = int(input('please enter second number:'))

    result = first_number + second_number
    print('result:', result)
except ValueError:
    print('please only enter only numbers')



print('continue or end the program')

# 2

try:
    first_number = int(input('please enter first number: '))
    second_number = int(input('please enter second number:'))

    result = first_number / second_number
    print('result:', result)
    open('C:\\my_file\\edu.txt')
except ValueError:
    print('please only enter only numbers')
except ZeroDivisionError:
    print('cannot divide by zero')
except Exception as err_msg:
    print('There is something wrong - contact admin - try later ')
    print(err_msg)
finally:
    print('this is finally statement - works any time')


print('continue or end the program')