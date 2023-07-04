def find_second_smallest(numbers):
    if len(numbers) < 2:
        return None

    smallest = float('inf')
    second_smallest = float('inf')

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest



my_list = [9, 2, 7, 3, 5, 1, 8]
second_smallest_num = find_second_smallest(my_list)

if second_smallest_num is None:
    print("There is no second smallest number in the list.")
else:
    print("Second smallest number:", second_smallest_num)
