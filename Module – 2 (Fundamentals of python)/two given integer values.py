def check_values(a, b):
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    else:
        return False

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check the values
result = check_values(num1, num2)

# Print the result
print("Result:", result)
