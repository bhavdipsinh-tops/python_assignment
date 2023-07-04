def remove_empty_tuples(list_of_tuples):
    result = [tuple_data for tuple_data in list_of_tuples if tuple_data]
    return result


my_list = [(1, 2), (), (3, 4), (), (), (5, 6, 7), ()]
filtered_result = remove_empty_tuples(my_list)

print("Original List:", my_list)
print("Filtered List:", filtered_result)
