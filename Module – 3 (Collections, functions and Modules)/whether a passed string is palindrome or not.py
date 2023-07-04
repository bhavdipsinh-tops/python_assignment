def is_palindrome(string):
    string = string.lower()  
    reversed_string = string[::-1]

    return string == reversed_string

word = "level"


is_palindrome_result = is_palindrome(word)
if is_palindrome_result:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
