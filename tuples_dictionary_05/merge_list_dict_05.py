# ex no.1 : # merge 2 lists into a single dictionary with key value

emp_ids_list = [101, 102, 103]
emp_names_list = ['ahmed', 'omar','sarah']

# solution : {101 : 'ahmed', 102 : 'omar' , 103 : 'sarah'}
person_dict = {}
# person_dict[101] = 'ahmed'
# person_dict[102] = 'omar'
# person_dict[103] = 'sarah'

for i in range(len(emp_ids_list)):
    person_dict[emp_ids_list[i]] = emp_names_list[i]

print(person_dict)