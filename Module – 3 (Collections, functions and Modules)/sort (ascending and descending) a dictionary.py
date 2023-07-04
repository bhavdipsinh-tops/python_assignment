def sort_dict_by_value(dictionary, reverse=False):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse))
    return sorted_dict

my_dict = {'apple': 5, 'banana': 2, 'orange': 10, 'kiwi': 1}

# Sort in ascending order
ascending_dict = sort_dict_by_value(my_dict)
print("Ascending Order:")
for key, value in ascending_dict.items():
    print(key, ":", value)

# Sort in descending order
descending_dict = sort_dict_by_value(my_dict, reverse=True)
print("Descending Order:")
for key, value in descending_dict.items():
    print(key, ":", value)
