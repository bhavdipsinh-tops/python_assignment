def check_keys_in_dictionary(dictionary, keys):
    for key in keys:
        if key not in dictionary:
            return False
    return True


my_dict = {'apple': 5, 'banana': 2, 'orange': 10}

# Check if keys exist
keys = ['apple', 'banana', 'kiwi']
if check_keys_in_dictionary(my_dict, keys):
    print("All keys exist in the dictionary.")
else:
    print("At least one key does not exist in the dictionary.")
