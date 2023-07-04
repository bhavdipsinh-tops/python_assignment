def replace_not_poor(string):
    not_index = string.find('not')
    poor_index = string.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return string[:not_index] + 'good' + string[poor_index + 4:]
    else:
        return string

input_string = input("Enter a string: ")


result = replace_not_poor(input_string)


print("Modified string:", result)
