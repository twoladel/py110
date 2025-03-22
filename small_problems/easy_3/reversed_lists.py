# def reverse_list(lst):
#     for i in range(len(lst)):
#         elem = lst.pop(0)
#         lst.insert(len(lst) - i, elem)
#     return lst

def reverse_list(lst):
    first = 0
    last = -1

    while first < (len(lst) // 2):
        lst[first], lst[last] = lst[last], lst[first]
        first += 1
        last -= 1
    return lst


list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True
