def replace_last_value(tuples_list, new_value):
    modified_list = []
    for tuple_data in tuples_list:
        modified_tuple = tuple_data[:-1] + (new_value,)
        modified_list.append(modified_tuple)
    return modified_list


my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 99
modified_result = replace_last_value(my_list, new_value)

print("Original List:", my_list)
print("Modified List:", modified_result)
