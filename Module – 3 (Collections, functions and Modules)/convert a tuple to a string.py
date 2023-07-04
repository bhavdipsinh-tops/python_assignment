def convert_tuple_to_string(tuple_data):
    string_data = ''.join(map(str, tuple_data))
    return string_data


my_tuple = (1, 2, 3, 4, 5)
string_result = convert_tuple_to_string(my_tuple)

print("Tuple:", my_tuple)
print("String:", string_result)
