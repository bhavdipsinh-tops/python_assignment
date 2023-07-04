def is_number_in_range(number, start, end):
    return start <= number <= end

num = 15
range_start = 10
range_end = 20

is_in_range = is_number_in_range(num, range_start, range_end)
if is_in_range:
    print(num, "is in the range.")
else:
    print(num, "is not in the range.")
