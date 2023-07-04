def contains_sublist(lst, sublist):
    n = len(sublist)
    return any((sublist == lst[i:i+n]) for i in range(len(lst)-n+1))

list1 = [1, 2, 3, 4, 5]
sublist1 = [2, 3]
sublist2 = [6, 7]

print("List:", list1)
print("Sublist [2, 3] is present?", contains_sublist(list1, sublist1))  # True
print("Sublist [6, 7] is present?", contains_sublist(list1, sublist2))  # False
