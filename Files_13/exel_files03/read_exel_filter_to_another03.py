# program to read from exel and filter data and write to another
import csv

with open("C:\\MY_FILE\\people.csv",'r') as my_file, open("C:\\MY_FILE\\people_new.csv", 'w', newline='') as my_file2:
    read_from_exel = csv.reader(my_file)
    write_to_exel = csv.writer(my_file2)
    write_to_exel.writerow(['Name', 'Age', 'City'])
    for row in read_from_exel:
        if row[2] == 'Cairo':
            write_to_exel.writerow(row)

