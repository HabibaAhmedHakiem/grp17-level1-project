# 4- Problem:
# Define a function extract_element(lst, index) that extracts an element at the specified index from a list lst.
# Handle the IndexError if the index is out of range.
# Sample Input: extract_element([1, 2, 3], 5)
# Expected Output: "Index out of range!“

def extract_element(lst, index):
    try:
        output = lst[index]
        return output
    except IndexError:
        return "Index out of range!"


output = extract_element([1, 2, 3], 5)

print(output)
