# Ex No. 2 : #
# 1 dict,                1 element in the list
person_list = [ { 101:'farouk', 102: 'marwa', 103: 'mostafa'} ]
print(person_list)    # print whole list
print(person_list[0])    # print dict  { 101:'farouk', 102: 'marwa', 103: 'mostafa'}

print(person_list[0][102])     # marwa
person_list[0][102] = 'marwa mahmoud'    # edit 'marwa' -> 'marwa mahmoud'
print(person_list)
print('____________________adding second dict to the list______________________')
dict2 =  { 104:'ibrahim', 105: 'usama'}
person_list.append(dict2)       # adding dict 2 as a new element in the list
print(person_list)
print(person_list[1])
person_list[1][105] = 'usama khalil'     # modify key 105 in dict 102 in the list
person_list[1][106] = 'Ehab'        # adding new employee to  dict2 in the list
print(person_list[1])
print(person_list)
