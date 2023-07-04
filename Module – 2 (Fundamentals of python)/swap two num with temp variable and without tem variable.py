# Swap using a temporary variable
def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Input numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Swapping using a temporary variable
num1, num2 = swap_with_temp(num1, num2)

print("After swapping (with temp variable):")
print("First number:", num1)
print("Second number:", num2)


print("*****************")

# Swap without using a temporary variable
def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Input numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Swapping without using a temporary variable
num1, num2 = swap_without_temp(num1, num2)

print("After swapping (without temp variable):")
print("First number:", num1)
print("Second number:", num2)
