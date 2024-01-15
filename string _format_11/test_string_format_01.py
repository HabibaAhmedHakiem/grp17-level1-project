# show all printing options
import math

emp_id = 101
emp_name = 'Esam Omar'
emp_salary = 58390.470538

print('---------------1. print with concat\n-------------------')
print('emps has id =' + str(emp_id) + ',his name is ' + emp_name +', \n\ttakes salary =' + str(emp_salary))

print('-----------2. print with malti parameters ---------------')
print('emp has id =', emp_id , ', his emp name ' , emp_name , 'takes salary = ', emp_salary)
print(150, 120, 200, 30, sep='-')
for i in range(10):
    print(i, end=' ')
print('\ntest')
print('test2')


print('---------------3.string formatting using placeholder------------ %s %d %f ---------')  # d = int  , f = float
print('Emp has id = %d, his name is %s, takes salary %f' %(emp_id, emp_name, emp_salary) )    # s = str
print('Emp has id = %d, his name is %s, takes salary %.2f' %(emp_id, emp_name, emp_salary) )


print('----------------4. string formatting using format function ----------------')
print('Emp has id = {}, his name is {}, takes salary {}'.format(emp_id, emp_name,emp_salary))
print('Emp has id = {:d}, his name is {:s}, takes salary {:f}'.format(emp_id, emp_name,emp_salary))
print('Emp has id = {:d}, his name is {:s}, takes salary {:.2f}'.format(emp_id, emp_name,emp_salary))
print('Emp has id = {:d}, his name is {:s}, takes salary {:,.2f}'.format(emp_id, emp_name,emp_salary))


print('-----------5. string formatting using F-string ------------')
print(F'Emp has id = {emp_id}, his name is = {emp_name}, takes salary = {emp_salary}')
print(F'Emp has id = {emp_id}, his name is = {emp_name}, takes salary = {emp_salary:f}')
print(F'Emp has id = {emp_id}, his name is = {emp_name}, takes salary = {emp_salary:.2f}')
print(F'Emp has id = {emp_id}, his name is = {emp_name}, takes salary = {emp_salary:,.2f}')

# --------------- Numbers Function : round, math.trank, math.ceil, math floor
emp_salary = 58390.670538
# 1. round
print(round(emp_salary,2))
print(F'using rounnd function, result = {round(emp_salary, 2)}')
print(F'using rounnd function, result = {round(emp_salary, 0)}')
# 2. math.trunk
print(math.trunc(emp_salary))
print(f'using trunk function, result = {math.trunc(emp_salary)}')
# 3. math.ciel ---> round to the high no in all cases
print(math.ceil(emp_salary))
print(f'using ciel function, result = {math.ceil(emp_salary)}')
# 4. math.floor ---> round to the low no in all cases
print(math.floor(emp_salary))
print(f'using the floor function, result = { math.floor(emp_salary)}')


