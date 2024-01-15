# program to read from exel and write back to list
import csv

peaple_list = []
with open("C:\\MY_FILE\\people.csv",'r') as my_file:
    read_from_exel = csv.reader(my_file)
    for line in read_from_exel:
        peaple_list.append(line)


    print(peaple_list)