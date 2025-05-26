'''Create a function that takes a list of numbers, all of which are the same 
except one. Find and return the number in the list that differs from all the rest.

The list will always contain at least 3 numbers, and there will always be 
exactly one number that is different.'''

'''
P-
input: list of integers
output: integer that is different from all others in the list

easy to do again with a dict of occurences and return the key with a value of 1

How do we check and short circuit?
check for return value from get of more than 1
check for dict of length two
if both then grab key associated with value of 1

for num in list
    add num to dict and check return value of setdefault
    if more than one and
    length of dict is 2
    loop over dict and get key associated with value of 1
'''

def what_is_different(numbers):
    num_counts = {}

    for num in numbers:
        num_counts[num] = num_counts.get(num, 0) + 1

    for key, value in num_counts.items():
        if value == 1:
            return key

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)