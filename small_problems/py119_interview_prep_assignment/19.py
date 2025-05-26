'''
Create a function that takes a list of integers as an argument and returns 
the integer that appears an odd number of times. There will always be exactly 
one such integer in the input list.
'''

'''
P-
input list of integers
output the integer in the list that appears an odd amount of times
    there will always be exactly one. 

A-
make a dict of char counts
find the value that is an odd number and return it's key
'''

def odd_fellow(numbers):
    int_counts = {}

    for num in numbers:
        int_counts.setdefault(num, 0)
        int_counts[num] += 1

    odd_one = [key for key, value in int_counts.items() if value % 2 != 0]
    return odd_one[0]

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)