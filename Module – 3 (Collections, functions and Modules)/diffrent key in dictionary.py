from itertools import product

def display_letter_combinations(dictionary):
    keys = sorted(dictionary.keys())
    values = [dictionary[key] for key in keys]
    combinations = list(product(*values))

    for combination in combinations:
        print(' '.join(combination))

my_dict = {'1': ['a', 'b'], '2': ['c', 'd']}

print("Letter Combinations:")
display_letter_combinations(my_dict)
