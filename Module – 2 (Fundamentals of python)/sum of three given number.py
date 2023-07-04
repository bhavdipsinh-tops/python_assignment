def sum_three_numbers(a, b, c):
    if a == b or b == c or c == a:
        return 0
    else:
        return a + b + c

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calculate the sum
result = sum_three_numbers(num1, num2, num3)

# Print the result
print("Sum:", result)
