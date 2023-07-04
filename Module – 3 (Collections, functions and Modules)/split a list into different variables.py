def split_list(lst):
    if len(lst) < 3:
        return None

    var1, *var2, var3 = lst
    return var1, var2, var3

my_list = [1, 2, 3, 4, 5]
result = split_list(my_list)

if result is None:
    print("The list must contain at least 3 elements.")
else:
    var1, var2, var3 = result
    print("Variable 1:", var1)
    print("Variable 2:", var2)
    print("Variable 3:", var3)
