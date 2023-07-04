def reverse_tuple(tuple_data):
    reversed_tuple = tuple(reversed(tuple_data))
    return reversed_tuple



my_tuple = (1, 2, 3, 4, 5)
reversed_result = reverse_tuple(my_tuple)

print("Tuple:", my_tuple)
print("Reversed Tuple:", reversed_result)
