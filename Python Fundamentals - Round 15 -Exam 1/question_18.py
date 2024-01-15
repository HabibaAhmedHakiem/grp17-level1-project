# swap 2 numbers in a program without using a temporary variable
def swap_num( x, y):
    x, y = y, x
    print('number 1 =', x ,'number 2 =', y )

number_1 = 11

number_2 = 65

swap_num(number_1,number_2)