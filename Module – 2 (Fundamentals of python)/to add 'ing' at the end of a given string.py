def add_suffix(string):
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    else:
        return string + 'ing'


input_string = input("Enter a string: ")

result = add_suffix(input_string)


print("Modified string:", result)
