# program to read from a file and write to another

with open("C:\\MY_FILE\\read_data.txt.txt",'r') as my_file:
    content = my_file.read()
    print(content)

with open("C:\\MY_FILE\\write_data.txt.txt",'w') as my_file:
    my_file.write(content)

