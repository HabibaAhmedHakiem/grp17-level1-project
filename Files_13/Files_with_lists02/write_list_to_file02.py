# program to write list into a file
my_list = ['luxor', 'Cairo', 'Alex']
output_file = "C:\\MY_FILE\\write_data.txt.txt"

with open(output_file, 'w') as my_file:
    for i in range(len(my_list)):
        if i == len(my_list) - 1:
            my_file.write(my_list[i])
        else:
            my_file.write(my_list[i] + '\n')

