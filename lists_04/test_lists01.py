# using lists
print('1. creating, printing list ')
numbers_list = [7, 12, 8, 20, 9, 14]
print(numbers_list)
print(type(numbers_list))

print('2. adding element to list [append function [ insert function ]') # index begins with 0
numbers_list.append(11)
numbers_list.insert(1,77)
print(numbers_list)

print('3. access element by index and change it')
print(numbers_list[4])
numbers_list[4] = 22    # changed it from 20 to 22
print(numbers_list)

print('4. count element of list (len function : general function)')
print(len(numbers_list))

print('5. delete element from the list -- remove, pop function --')
numbers_list.remove(9)  # delete the element (9)
numbers_list.pop(4)  # delete at index [4] ----> (22)          # numbers_list.pop() : remove last element
print(numbers_list)

print('6. reverse list')
numbers_list.reverse()
print(numbers_list)

print('7.sort list')
#  numbers_list.sort() ------> sort from small to big
numbers_list.sort()
print(numbers_list)
#  numbers_list.sort(reverse= True) ----> sort from big to small
numbers_list.sort(reverse= True)
print(numbers_list)