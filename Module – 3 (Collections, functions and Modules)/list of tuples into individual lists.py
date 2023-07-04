def unzip_list_of_tuples(list_of_tuples):
    unzipped_lists = list(zip(*list_of_tuples))
    return unzipped_lists


my_list = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
unzipped_result = unzip_list_of_tuples(my_list)

print("Original List:", my_list)
print("Unzipped Lists:")
for i, sublist in enumerate(unzipped_result):
    print(f"List {i+1}: {sublist}")
