'''Create a function that takes a list of integers as an argument. 
Determine and return the index N for which all numbers with an index less than 
N sum to the same value as the numbers with an index greater than N. If there 
is no index that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the 
smallest value.

The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the 
numbers to the right of the last element is 0.'''


'''
P-
return the index where sums to left and right of said index, not inclusive
are equal

input list of integers
output integer - index

left of index 0 right of last index are both 0
-1 if no equal sums
return first index this occurs (break when we have equal sums)

summing two sublists or slices of the list and comparing them
return the index when it is equal

D-
lists and slices
sum function
loop

A-
for each index
    sum the list slice below and above that index, exclusive of the current index
    if sums are equal break and return current index

if no equal sums return -1
'''

def equal_sum_index(numbers):
    for idx in range(len(numbers)):
        left_sum = sum(numbers[:idx])
        right_sum = sum(numbers[idx + 1:])

        if left_sum == right_sum:
            return idx
        
    return -1
        

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)