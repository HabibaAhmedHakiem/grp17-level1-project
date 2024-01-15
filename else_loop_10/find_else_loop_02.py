# find if a no. is found in list - print it's first index
# or print .. no. is not found using a flag

my_list = [14, 5, 22, 10, 30]
num = 22

for item in my_list:
    if num == item:
        print('no is found at index =', my_list.index(num))
        break
else:
    print('no is not found')