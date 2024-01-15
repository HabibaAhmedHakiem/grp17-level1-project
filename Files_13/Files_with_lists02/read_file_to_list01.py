# the program to read from text file and put data into a list

input_file = "C:\\MY_FILE\\read_data.txt.txt"
new_lines_list = []

with open(input_file, 'r') as my_file:
    lines_list = my_file.readlines()
    for line in lines_list:
        line = line.strip()
        if line != '':
            new_lines_list.append(line)


print(new_lines_list)





