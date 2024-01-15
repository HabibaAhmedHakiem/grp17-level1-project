# program to check for person age
# inputs
person_name = 'habiba hakiem'
person_age =input('please enter your age ')
person_age = int(person_age)

#processing ( calcluation )
if person_age > 16:
    print('you are a man')

# elif person_age >= 11 and person_age <= 16: or elif person_age >= 11 : <---- this is better
elif person_age >= 11:
    print('you are a boy')
else:
    print('you are a child')


