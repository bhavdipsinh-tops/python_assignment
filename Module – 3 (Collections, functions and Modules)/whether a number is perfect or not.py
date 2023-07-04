def is_perfect_number(number):
    if number <= 0:
        return False

    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    divisor_sum = sum(divisors)
    return divisor_sum == number

num = 28

is_perfect = is_perfect_number(num)
if is_perfect:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
