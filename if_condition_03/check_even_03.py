#program to check for even odd :
# (%) ---> mod/ modulos / reminder باقي القسمة
print( 4 / 2 ) # divided = 2
print( 4 % 2 ) # mod reminder = 0
print( 11 % 2 ) # 1
print( 437 % 3 ) # 2
# 14 month :how many years - how many remainig month ?
print('years ', int( 14 / 12 ))
print('remaining months ', int( 14 % 12))

# num = input('please enter your no') \ num = int(num) or enter a no (a variable with a constant no )
num = input('please enter your no')
num = int(num)

if num % 2 == 0:
    print('it is even no. ')
else:
    print('it is odd no. ')
