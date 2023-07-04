def print_unique_values(dictionary):
    unique_values = set(dictionary.values())
    for value in unique_values:
        print(value)

my_dict = {'apple': 5, 'banana': 2, 'orange': 10, 'kiwi': 5, 'mango': 10}

# Print unique values
print("Unique Values:")
print_unique_values(my_dict)
