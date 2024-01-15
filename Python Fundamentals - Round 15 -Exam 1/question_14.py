# Remove all characters except letters and numbers
ini_string = '123abcjw:, .@! eiw'
def delete_special(statement):
    new_string = ''
    for item in statement:
        if item.isalnum():
            new_string = new_string + item
    return new_string

ans = delete_special(ini_string)

print(ans)