def get_unique_values(lst):
    unique_values = list(set(lst))
    return unique_values


original_list = [1, 2, 2, 3, 3, 4, 4, 5]
unique_values = get_unique_values(original_list)

print("Original List:", original_list)
print("Unique Values:", unique_values)
