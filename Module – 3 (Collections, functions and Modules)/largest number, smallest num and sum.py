def analyze_numbers(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    return largest, smallest, total


list1 = [2, 33, 222, 14, 25]
largest_num, smallest_num, sum_of_all = analyze_numbers(list1)

print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
print("Sum of all numbers:", sum_of_all)
