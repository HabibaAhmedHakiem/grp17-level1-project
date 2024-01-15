# program to write into text file

"""
1- Open for write
2- Write
3- Close

"""

print('..............First Way................')
my_file = open("C:\\Users\\habiba\\Desktop\\MY_FILE\\write_data.txt.txt",'w')
my_file.write('I like programming\n')
my_file.write('I like football\n')
my_file.write('Python is a programming language')
my_file.close()


print('..............Second Way.......writing with .....')
with open("C:\\Users\\habiba\\Desktop\\MY_FILE\\write_data.txt.txt",'a') as my_file:   # 'w' write  'a' append
    my_file.write('\n')
    my_file.write('My City is Cairo\n')
    my_file.write('My City is Alex\n')
    my_file.write(' Iam a SW Engineer')


