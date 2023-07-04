def find_highest_values(dictionary, n=3):
    sorted_values = sorted(dictionary.values(), reverse=True)
    highest_values = sorted_values[:n]
    return highest_values

my_dict = {'apple': 5, 'banana': 10, 'orange': 3, 'kiwi': 8, 'mango': 12}

highest_values = find_highest_values(my_dict)
print("Highest 3 Values:")
print(highest_values)
