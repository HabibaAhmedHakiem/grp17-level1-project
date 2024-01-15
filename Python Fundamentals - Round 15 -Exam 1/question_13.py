#  Check if an element exists in a list in Python and return all occurrence indexes of the element in this list
def find_double( my_list , num ):
    list_test =[]
    for test_no in range(len(my_list)):
        if my_list[test_no] == num:
            list_test.append(test_no)
    return list_test

my_list =[ 12, 16, 14, 16, 17, 16, 19 ]

num = 16

ans = find_double( my_list , num )
print(ans)

