def create_dictionary_from_string(string):
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

input_string = 'w3resource'

result_dict = create_dictionary_from_string(input_string)
print("Dictionary:")
print(result_dict)
