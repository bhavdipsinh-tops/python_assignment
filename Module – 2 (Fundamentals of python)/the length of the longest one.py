def find_longest_word_length(word_list):
    longest_length = 0

    for word in word_list:
        if len(word) > longest_length:
            longest_length = len(word)

    return longest_length


words = ["apple", "banana", "cherry", "durian", "elderberry"]
result = find_longest_word_length(words)
print("Length of the longest word:", result)
