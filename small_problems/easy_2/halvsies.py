''' PEDAC for this problem
P-
We're halving an argument list into two lists
input: a list
output: nested list with two inner lists each containing half the original list
Explicit:
    - maintain original order
    - if input list len is odd, middle element goes in first half
Implicit:
    - empty list should return two empty nested lists inside outer list
    - single element list should return single element in first half list
        - and second half list is empty
Questions:
    - empty list? - answered by examples
    - single element list? answered by examples
    - how would we treat nested collections? As single elements?
    - is this supposed to be a mutated list? or new object?

E- 
examples clarified two of my questions

D- 
input: list
output: 2 lists inside a list
intermediate: build the inner lists and then wrap in a list?

A-
High level:
    create new empty list for return value
    Half the list
        Determine length of list
        Divide by 2
            if length is even, this is how many elements in each list
                ie - the end of the list slice, since we start at 0
            if length is odd, quotient plus 1 is len of first half list 
    Put elements in two new lists
        new list variables that capture half slices of original list
    append first half and then second half to new list
    return new list
'''

def find_list_middle(lst):
    if len(lst) % 2 == 0:
        middle = len(lst) // 2
    else:
        middle = (len(lst) // 2) + 1
    return middle

def halvsies(lst):

    stop_first_half = find_list_middle(lst)
    first_half = lst[:stop_first_half]
    second_half = lst[stop_first_half:]

    return [first_half, second_half]
    

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])