def check_element_in_tuple(element, tuple_data):
    if element in tuple_data:
        return True
    else:
        return False

    
my_tuple = (1, 2, 3, 4, 5)
element1 = 3
element2 = 6

print("Tuple:", my_tuple)
print("Does", element1, "exist in the tuple?", check_element_in_tuple(element1, my_tuple))  # True
print("Does", element2, "exist in the tuple?", check_element_in_tuple(element2, my_tuple))  # False
