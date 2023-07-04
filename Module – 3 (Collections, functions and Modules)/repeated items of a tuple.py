def find_repeated_items(tuple_data):
    repeated_items = []
    unique_items = set()
    for item in tuple_data:
        if item in unique_items:
            repeated_items.append(item)
        else:
            unique_items.add(item)
    return repeated_items


my_tuple = (1, 2, 3, 4, 2, 5, 3, 6)
repeated_result = find_repeated_items(my_tuple)

print("Tuple:", my_tuple)
print("Repeated Items:", repeated_result)
