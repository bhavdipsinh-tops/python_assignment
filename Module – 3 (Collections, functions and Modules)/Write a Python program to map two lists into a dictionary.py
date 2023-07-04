def map_lists_to_dictionary(keys, values):
    mapped_dict = dict(zip(keys, values))
    return mapped_dict


keys = ['name', 'age', 'country']
values = ['Bhavdip', 25, 'India']


mapped_dict = map_lists_to_dictionary(keys, values)
print("Mapped Dictionary:")
print(mapped_dict)
