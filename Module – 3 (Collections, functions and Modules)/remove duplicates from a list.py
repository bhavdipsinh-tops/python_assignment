def remove_duplicates(lst):
    return list(set(lst))

original_list = [1, 2, 3, 3, 4, 4, 5, 6, 6]
result = remove_duplicates(original_list)

print("Original List:", original_list)
print("List after removing duplicates:", result)
