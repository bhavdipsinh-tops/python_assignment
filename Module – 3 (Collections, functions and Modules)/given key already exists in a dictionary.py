def check_key_in_dictionary(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

my_dict = {'apple': 5, 'banana': 2, 'orange': 10}

# Check if key exists
key = 'banana'
if check_key_in_dictionary(my_dict, key):
    print(f"The key '{key}' exists in the dictionary.")
else:
    print(f"The key '{key}' does not exist in the dictionary.")
