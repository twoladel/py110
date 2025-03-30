'''
Function should return a list with all elements multiplied by two.

The augmented assignment statement on line 3 of the function definition changes
the value of the local variable item, but the function does not do anything 
with that value. Ints are immutable, so we need to:
    1. reassign the list element by referencing its index 
    or 
    2. append the new int object referenced by item to a new list object
    (this second option we can do with a list comprehension). 
'''

def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6]) # False


def multiply_list(lst):
    '''Mutates the original list in place'''
    for idx, item in enumerate(lst):
        lst[idx] = item * 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6]) # True


def multiply_list(lst):
    '''Creates a new list object and returns it.'''
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6]) # True
