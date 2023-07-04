from collections import Counter

def combine_dictionaries(d1, d2):
    combined_dict = Counter(d1) + Counter(d2)
    return combined_dict


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries and add values for common keys
combined_dict = combine_dictionaries(d1, d2)
print("Combined Dictionary:")
print(combined_dict)
