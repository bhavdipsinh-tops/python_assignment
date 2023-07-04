def find_max_min(numbers):
    if len(numbers) == 0:
        return None

    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num


decimal_numbers = [3.14, 2.71, 1.618, 0.577, 2.718, 4.669]
max_value, min_value = find_max_min(decimal_numbers)

print("Maximum number:", max_value)
print("Minimum number:", min_value)
