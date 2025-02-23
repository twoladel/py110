'''
P-
merge two lists alternating back and forth between them
input: two lists
output: new list object, contains all elements from both passed lists.
Explicit:
    - elements being selected into new list must alternate back and forth
    - won't be given empty lists
    - lists will be the same size
Implicit:
    - first list arg, should be element[0] of new list object

Questions: Does it matter if we mutate the original lists?
    - two different solutions below to account for each possibility
D- lists
A- 
define an empty list
While lists are NOT empty
    remove first element in list1 and append to new list
    then do same for list2
return new list
'''
def interleave(lst1, lst2): # This version empties (mutates) the original lists
    new_list = []

    while lst2:
        new_list.append(lst1.pop(0))
        new_list.append(lst2.pop(0))
    return new_list

# def interleave(lst1, lst2): # This version retains the original lists.
#     new_list = []

#     for i in range(len(lst1)):
#         new_list.append(lst1[i])
#         new_list.append(lst2[i])
#     return new_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)   # True