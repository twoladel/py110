'''
P-
input: unordered list of values
ouput: the value that appears more than once
Explicit:
    only one value will appear more than once (exactly twice)
    all other values only occur once
    will always have one duplicate value
Implicit:
    don't have to worry about empty lists

E-
Seems we'll only be working with integers

D- input is list
ouput is an object in these examples integers
temp variable for counting?

A- 
Find the duplicated value
    loop through the list
    call count method on each value
    if 2 is returned
        break
        return value
Return it

Would sorting make this solution more efficient?
'''
def find_dup(lst):
    for element in lst:
        if lst.count(element) == 2:
            return element


print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True