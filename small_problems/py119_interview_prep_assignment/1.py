'''Create a function that takes a list of numbers as an argument. 
For each number, determine how many numbers in the list are smaller than it, 
and place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs 
multiple times in the list, it should only be counted once.'''

'''
P-
input: list of integers
output: list of integers, where ints are counts of values smaller than the current value

list should be same len as input list
don't include dupes in count, for example 8 can't be greater than 2 twice

D-
lists
sets

A-
create an empty result list

for each number in the list
    get a sublist of other numbers with slicing
    convert to a set
    set counter variable
    for each element in the set
        if current num greater
            increment count
    append the count to a result list
'''

def smaller_numbers_than_current(numbers):
    result = []

    for idx, number in enumerate(numbers):
        distinct_nums = set(numbers[:idx] + numbers[idx + 1:])
        count = 0
        
        for num in distinct_nums:
            if number > num:
                count += 1
        
        result.append(count)
    return result

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)