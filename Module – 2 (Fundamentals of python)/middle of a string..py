def insert_string_in_middle(original_string, insert_string):
    mid_index = len(original_string) // 2
    return original_string[:mid_index] + insert_string + original_string[mid_index:]

# Test case
original = "Hello World"
to_insert = "beautiful "
result = insert_string_in_middle(original, to_insert)
print(result)  # Output: "Hello beautiful World"
