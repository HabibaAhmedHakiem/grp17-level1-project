# program to solve net salary
emp_name = 'habiba ahmed'
emp_gross_salary = 100000

# processing (caculation )
if emp_gross_salary >= 5000:
    tax_pct = 10
else:
    tax_pct = 0

emp_net_salary = emp_gross_salary - tax_pct / 100 * emp_gross_salary

#output :result
print('Emp net salary \n=', emp_net_salary)
