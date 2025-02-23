'''
P-
input: list of positive ints
output: numerical string formatted to 3 decimals
Explicit:
    all elements are positive ints (>0)
    multiply all ints in list together
    Divide that number by amount of ints in list
    convert to string
Implicit:
    list won't be empty
    will contain at least two values


A-
multiply all ints in list together
Divide that number by amount of ints in list
convert to string / format float to 3 decimal places
return
'''

def multiplicative_average(numbers):
    product = 1
    for element in numbers:
        product *= element

    result = product / len(numbers)
    return f'{result:.3f}'

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")