#Using the dict() constructor:

my_list = [("a", 1), ("b", 2), ("c", 3)]
my_dict = dict(my_list)
print(my_dict)

#Using dictionary comprehension

my_list = [("a", 1), ("b", 2), ("c", 3)]
my_dict = {key: value for key, value in my_list}
print(my_dict)
