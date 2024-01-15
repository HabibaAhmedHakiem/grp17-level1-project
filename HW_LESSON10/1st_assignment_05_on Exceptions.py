# 5- Problem:
# Create a function fetch_element(dictionary, key) that fetches a value from a dictionary based on the provided key.
# Handle the KeyError if the key does not exist in the dictionary.
# Sample Input: fetch_element({'a': 1, 'b': 2}, 'c')
# Expected Output: "Key 'c' not found in the dictionary!"

def fetch_element(dictionary, key):
    try:
        value = dictionary[key]
        return value
    except KeyError:
        return print('key', key, 'not found in dictionary !')  # or f"Key '{key}' not found in the dictionary!"


output = fetch_element({'a': 1, 'b': 2}, 'c')


print(output)
