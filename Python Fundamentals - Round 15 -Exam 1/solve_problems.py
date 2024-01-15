#question_11

def valid_pass(pass_value):
    if len(pass_value) < 8:
        return False
    small_letter, capital_letter, special_letter, count_no = 0, 0, 0, 0

    for letter in pass_value:
        if letter.islower():
            small_letter = small_letter + 1
        elif letter.isupper():
            capital_letter = capital_letter + 1
        elif letter.isdigit():
            count_no = count_no + 1
        elif letter in '_@$':
            special_letter = special_letter + 1
    return all([small_letter > 0, capital_letter > 0, count_no > 0, special_letter > 0])

password = "ha_4545Aahmed"
result = valid_pass(password)

if result:
    print("Password is fine")
else:
    print("Password is not fine")

# question_12

def reverse_string(statement):
    word_reverse = statement.split()
    reversed_statement = ' '.join(reversed(word_reverse))
    return reversed_statement

str = 'hello my name is habiba ahmed'

ans = reverse_string(str)

print(ans)


# question_13

def find_double( my_list , num ):
    list_test =[]
    for test_no in range(len(my_list)):
        if my_list[test_no] == num:
            list_test.append(test_no)
    return list_test

my_list =[ 12, 16, 14, 16, 17, 16, 19 ]

num = 16

ans = find_double( my_list , num )
print(ans)


# question_14

ini_string = '123abcjw:, .@! eiw'
def delete_special(statement):
    new_string = ''
    for item in statement:
        if item.isalnum():
            new_string = new_string + item
    return new_string

ans = delete_special(ini_string)

print(ans)


# Question_15

ips_List = [

    ('192.168.0.15', 'y'),

    ('192.168.0.22', 'y'),

    ('192.168.0.14', 'y'),

    ('192.168.0.24', 'n'),

    ('192.168.0.15', 'y'),

    ('192.168.0.11', 'y')]

company_list_2 = []

for item in ips_List:
    if item not in company_list_2:
        company_list_2.append(item)


print(company_list_2)

# Question_16

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


# Question_17

shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
total_sum = 0

for key, value in shopping_cart_dict.items():
    shopping_cart_dict[key] = value + value * 10/100
    total_sum = total_sum + shopping_cart_dict[key]

print('After 10% raise: ', shopping_cart_dict)
print('Total sum: ', total_sum)


sum_net_value = total_sum + total_sum * 14/100
print('Net value = ', sum_net_value)

# Question_18

def swap_num( x, y):
    x, y = y, x
    print('number 1 =', x ,'number 2 =', y )

number_1 = 11

number_2 = 65

swap_num(number_1,number_2)

# Question_19

ips_list = [
('192.168.0.15', 'y'),
('192.168.0.22', 'y'),
('192.168.0.14', 'y'),
('192.168.0.24', 'n'),
('192.168.0.81', 'n'),
('192.168.0.11', 'y')]

for code, num in ips_list:
    if num == 'y':
        print( code , '=' , code[-2:] )


# Question_20

str = "my name is habiba habiba is my name hi habiba"

str_list = str.split()

print(str_list)

times_ouccurred = str.count('habiba')

print('occurrences of a word habiba =',times_ouccurred)