def get_string_chars(string):
    if len(string) < 2:
        return ""
    else:
        return string[:2] + string[-2:]


input_string = "Hello, World!"
result = get_string_chars(input_string)
print(result)  # Output: "Held"

input_string = "Hi"
result = get_string_chars(input_string)
print(result)  # Output: "Hi"

input_string = "A"
result = get_string_chars(input_string)
print(result)  # Output: ""
