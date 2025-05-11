'''Create a function that takes a list of integers as an argument and 
returns a tuple of two numbers that are closest together in value. 
If there are multiple pairs that are equally close, return the pair that 
occurs first in the list.'''

'''
P-
input list of integers
output tuple of two integers that are closest in value from input list

rule: if two pairs same diff, use first pair that occured

return closest pair from a list of numbers

D-
lists 
tuples

A-
set tuple to first two elements

for each number compare with each number after it
if difference between two numbers is lower
update the tuple

return tuple
'''

def closest_numbers(numbers):
    result = (numbers[0], numbers[1])

    for idx in range(len(numbers)):
        for index in range(idx + 1, len(numbers)):
            if abs(numbers[idx] - numbers[index]) < abs(result[0] - result[1]):
                result = (numbers[idx], numbers[index])

    return result

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))