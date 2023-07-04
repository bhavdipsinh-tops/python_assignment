def convert_to_dictionary(list_of_tuples):
    dictionary = dict(list_of_tuples)
    return dictionary


my_list = [("a", 1), ("b", 2), ("c", 3)]
dictionary_result = convert_to_dictionary(my_list)

print("Original List of Tuples:", my_list)
print("Dictionary:", dictionary_result)
