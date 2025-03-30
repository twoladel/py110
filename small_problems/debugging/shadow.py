def mutltiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(mutltiply_sum(numbers, 2) == 20) # True

'''Original code to refactor below. Example of why you shouldn't name your
functions the same as already existing built-ins. Renamed the function
above to handle the issue.'''

def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20) # False