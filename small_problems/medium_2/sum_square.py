'''
P-
returning the difference of a mathematical expression. Getting a positive int
and we're summing all the positive ints to inclusive of the argument int and
squaring that sum. Then getting the sum of all the squares of that series of 
positive ints and subtracting it from squaring the sum. 

ints 
range

A-
sum a range inclusive of the arg int
square that sum and assign it to squared_sum variable

list comp to create a list of squares for all numbers in the sequence
inclusive of the arg int and sum that list
and assign it to a variable summed_squares

return the difference (squared_sum - summed_squares)
'''
def sum_square_difference(count):
    squared_sum = sum(range(1, count + 1)) ** 2
    
    summed_squares = sum([num ** 2 for num in range(count + 1)])
    return squared_sum - summed_squares

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True