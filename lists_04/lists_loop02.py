numbers_list = [7, 12, 8, 20, 9, 14, 9]
# use index

sum_list =0
print('1. for i loop')
for i in range(len(numbers_list)):
    print(i,'-->', numbers_list[i])
    sum_list = sum_list + numbers_list[i] # accumulative sum equation
print(' sum of elements = ', sum_list)

print('2.for each loop[for in loop ---> doesnt use list index ]')
sum_list = 0 # reset variable
for item in numbers_list:
    print(item)
    sum_list = sum_list + item
print(' sum of elements = ', sum_list)

print('=======using  general function sum()========')
print(sum(numbers_list))


