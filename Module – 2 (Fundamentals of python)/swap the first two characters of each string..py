def swap_first_two_characters(string):
    if len(string) >= 2:
        return string[1] + string[0] + string[2:]
    else:
        return string

def combine_strings(string1, string2):
    swapped_string1 = swap_first_two_characters(string1)
    swapped_string2 = swap_first_two_characters(string2)
    combined_string = swapped_string2 + " " + swapped_string1
    return combined_string


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


result = combine_strings(string1, string2)

print("Combined string with swapped characters:", result)
