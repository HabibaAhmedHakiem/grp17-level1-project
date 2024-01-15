# Count and print no. of Male, no. of Female in the list of Tuples

company_employees = [
    (101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
    (102, 'Ibrahim Ahmed', 9000.0, 'Accountant', 'M'),
    (103, 'Adham Aly', 5000.0, 'Engineer', 'M'),
    (104, 'Islam Hassan', 7000.0, 'Sales', 'M'),
    (105, 'Marwa Esam', 7000.0, 'Marketer', 'F'),
    (106, 'Ola Hassan', 7000.0, 'Engineer', 'F')]

no_male_count = 0
no_female_count = 0

for item in company_employees:
    Gender = item[4]
    if Gender == 'M':
        no_male_count = no_male_count + 1
    else:
        no_female_count = no_female_count + 1

print('No of Male employees:', no_male_count, 'No of Female employees:', no_female_count)

