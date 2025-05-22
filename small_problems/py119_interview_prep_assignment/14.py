'''Create a function that takes a single integer argument and returns the sum 
of all the multiples of 7 or 11 that are less than the argument. If a number 
is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, 
and 22. The sum of these multiples is 75.

If the argument is negative, return 0.'''

'''
P-
input: integer that is a range to be iterated over
output: integer, sum of all mulitples of 7 or 11 within the range

If multiple of both, only count it once (use or selection)

if arg is less than 7, return 0

iterate over a range, but we can start at 7 since it is the first multiple
multiple means evenly divisible by (modulo)

D-
sum function
list comp selection

A-
guard clause for inputs less than 7

return the sum of a list comp

the loop in the list comp will be 
for number in range 7 to the input integer
select the number if it is evenly divisible by 7 or 11 
'''

def seven_eleven(number):
    if number < 7:
        return 0
    
    return sum([
        num for num in range(7, number)
        if num % 7 == 0 or num % 11 == 0])

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)