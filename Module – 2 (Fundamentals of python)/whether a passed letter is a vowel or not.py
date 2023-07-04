def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter.lower() in vowels:
        return True
    else:
        return False

letter = input("Enter a letter: ")

if len(letter) == 1 and letter.isalpha():
    if is_vowel(letter):
        print(letter, "is a vowel.")
    else:
        print(letter, "is not a vowel.")
else:
    print("Invalid input. Please enter a single letter.")
