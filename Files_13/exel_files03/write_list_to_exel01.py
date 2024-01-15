# program to write a list to exel file
import csv

people_list = [
    ['name', 'age', 'city'],
    ['adham', '25', 'Alex'],
    ['Esam', '30', 'cairo'],
    ['shady', '28', 'Mansoura']
]
with open("C:\\MY_FILE\\people.csv",'w', newline='') as my_file:
    write_to_excel = csv.writer(my_file)
    for i in people_list:
        write_to_excel.writerow(i)
