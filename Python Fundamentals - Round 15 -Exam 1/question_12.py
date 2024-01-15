# program to reverse a string words

def reverse_string(statement):
    word_reverse = statement.split()
    reversed_statement = ' '.join(reversed(word_reverse))
    return reversed_statement

str = 'hello my name is habiba ahmed'

ans = reverse_string(str)

print(ans)