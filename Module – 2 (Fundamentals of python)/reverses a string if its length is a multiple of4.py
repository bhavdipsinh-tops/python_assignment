def reverse_string_if_multiple_of_four(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string




#example


input_string = "Hello, World!"
result = reverse_string_if_multiple_of_four(input_string)
print(result)
