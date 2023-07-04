def generate_squared_list():
    squared_list = [num ** 2 for num in range(1, 31)]
    first_5 = squared_list[:5]
    last_5 = squared_list[-5:]
    return first_5, last_5



first_5_elements, last_5_elements = generate_squared_list()

print("First 5 elements:", first_5_elements)
print("Last 5 elements:", last_5_elements)
