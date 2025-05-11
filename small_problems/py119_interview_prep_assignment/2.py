'''Create a function that takes a list of integers as an argument. 
The function should return the minimum sum of 5 consecutive numbers 
in the list. If the list contains fewer than 5 elements, 
the function should return None.'''

'''
P-
input list of integers
output: integer, which is min sum of 5 consecutive numbers. 

list len < 5, return None

summing sublists and updating a minimum sum as we go

D-
sum function
min_sum variable
slicing
nested loop?
only iterating length of list minus length of sublist

A-
if length of list less than 5, return None

create min_sum variable = 100 or float('inf')

find sublists
for start in range(len(list) - 4)
    get slice from start to start + 5
    sum that slice
    compare to min
    if smaller update

return min_sum

'''

def minimum_sum(numbers):
    if len(numbers) < 5:
        return None
    
    min_sum = float('inf')
    
    for start in range(len(numbers) - 4):
        current_sum = sum(numbers[start:start + 5])
        if current_sum < min_sum:
            min_sum = current_sum

    return min_sum

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)