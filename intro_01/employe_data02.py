# program to show employee data
emp_id = 101  # int data type
emp_name = "Ahmed Amr"  # string data type
emp_salary = 7000.55 # float data type
emp_job = 'python developer'  # string data type

# concat : Ahmed Amr works as python developer
print(emp_name + ' works as '+ emp_job)

# concat : Ahmed Amr id = 101
print(emp_name + ' id = ' + str(emp_id))
# CASTING:  changing from data type to another (str to float,int to str,float to str,...). It is coverted
# only in this command.
print(emp_name+ ' takes salary = ' + str(emp_salary))
print('...........from float to int.........')
print(int(emp_salary)) # removes fractions
#For rounding a float "round" to int