'''Create a function that takes a string of digits as an argument and returns 
the number of even-numbered substrings that can be formed. For example, in the 
case of '1432', the even-numbered substrings are '14', '1432', '4', '432',
'32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a 
separate substring.'''

'''
P-
input is a string of digits
output integer, count of substrings that are even. 

Count every occurence of a substring, even if it appears twice.
Must be EVEN-numbered (%2 == 0)

The last digit in any substring that is even means the substring is even.

D-
list of ints

A-
create a counter variable
list comp to get a list of ints
while the list is not empty
    check the last number
    if even
        increment count by length
    remove last number (pop)
        
return the count
'''

def even_substrings(string):
    digits = [int(digit) for digit in string]

    count = 0

    while digits:
        if digits[-1] % 2 == 0:
            count += len(digits)
        digits.pop()

    return count


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)