def fibonacci_range(n):
    fib_series = []
    a, b = 0, 1

    while a <= n:
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

range_limit = int(input("Enter the range limit: "))

fibonacci_series = fibonacci_range(range_limit)
print("The Fibonacci series up to", range_limit, "is:")
print(fibonacci_series)
