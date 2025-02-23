'''
P-
input: two lists - each contain numbers
output: NEW list of products 
Explicit
    both lists will be same length
    operands for multiplying will be same index from each list
        ie index 0 of list 1 times index 0 of list 2, etc
implicit
    lists won't be empty
    return list will be same length as input list

D- lists
comprehension for output?

A-
create new empty list
for each index
    multiply the elements at matching indices
    append product to new list
return new list
'''
def multiply_list(lst1, lst2):
    return [tup[0] * tup[1] for tup in zip(lst1, lst2)]

# Alternate solution:
# def multiply_list(lst1, lst2):
#     return [a * b for a, b in zip(lst1, lst2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

list3 = [6, 10, 50]
list4 = [6, 55, -3]
print(multiply_list(list3, list4))