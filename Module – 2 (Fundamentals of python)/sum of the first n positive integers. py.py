def sum_of_positive_integers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Get input from the user
n = int(input("Enter a positive integer: "))

# Calculate the sum
result = sum_of_positive_integers(n)

# Print the result
print("Sum of the first", n, "positive integers:", result)
