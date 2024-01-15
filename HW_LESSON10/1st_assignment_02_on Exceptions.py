# 2- Problem: Create a function calculate_average(num_list) that calculates the average of numbers in a list.
# Handle the TypeError exception if a non-numeric value is present in the list and return a message.
# Sample Input: calculate_average([10, 20, '30z', 40])
# Expected Output: "Error: Non-numeric value found in the list!"

def calculate_average(num_list):
    try:
        numeric_values = [float(number) for number in num_list if isinstance(number, (int, float))]

        if numeric_values:
            average = sum(numeric_values) / len(numeric_values)
            return average
        else:
            return "Error: No numeric values found in the list!"
    except TypeError:
        return "Error: Non-numeric value found in the list!"


output = calculate_average([10, 20, '30z', 40])

print(output)
