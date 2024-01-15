# find if a no. is found in list - print it's first index
# or print .. no. is not found using a flag

my_list = [14, 5, 22, 10, 30]
num = 22

is_found = False
for item in my_list:
    if item == num:
        print('no is found at index',my_list.index(item))
        is_found = True


if is_found == False:
    print('no is not found')