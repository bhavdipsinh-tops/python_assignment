def count_word_occurrences(sentence):
    word_count = {}

    
    words = sentence.split()

    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


input_sentence = input("Enter a sentence: ")


result = count_word_occurrences(input_sentence)


print("Word occurrences:")
for word, count in result.items():
    print(f"{word}: {count}")
