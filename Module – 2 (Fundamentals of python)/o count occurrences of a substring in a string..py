def count_substring_occurrences(string, substring):
    count = 0
    index = 0

    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        count += 1
        index += len(substring)

    return count

input_string = input("Enter a string: ")
input_substring = input("Enter a substring to count: ")


result = count_substring_occurrences(input_string, input_substring)


print("Occurrences of substring:", result)
