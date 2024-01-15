# program to creat random game
import random

count_correct = 0
count_wrong = 0
for i in range(5):
    first_no = random.randint(1, 100)
    second_no = random.randint(1, 100)
    print(first_no, ' + ', second_no, ' = ')
    user_result = input()  # don't forget to switch from string to int
    user_result = int(user_result)
    correct_result = first_no + second_no
    if user_result == correct_result:
        print('congrats correct answer')
        count_correct = count_correct + 1 # incemental
    else:
        print('failed, wrong answer')
        count_wrong = count_wrong + 1 # incremental
print('count correct = ', count_correct)
print('count wrong = ', count_wrong)
print('end of the program')
