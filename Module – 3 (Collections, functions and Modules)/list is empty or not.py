def is_list_empty(lst):
    if not lst:
        return True
    else:
        return False



list1 = []  #empty list
list2 = [1, 2, 3]  #non-empty list

print("Is list1 empty?", is_list_empty(list1))
print("Is list2 empty?", is_list_empty(list2))
