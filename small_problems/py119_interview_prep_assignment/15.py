'''Create a function that takes a string argument that consists entirely of 
numeric digits and computes the greatest product of four consecutive digits 
in the string. The argument will always have more than 4 digits.'''

'''
P-
input string of digits
output integer, greatest product of 4 consecutive digits

taking substrings of lenght 4 and multiplying all elements together

D-
greatest product variable (should be set to 1)
current product variable to compare against greatest
easier to work with a list

A-
convert string to list of ints (list comp)

iterate over the ints
start index is upto length of input string minus 3. then we can stop iterating.
capture sublist
pass sublist to a helper function

helper function
iterates over sublist and returns product

compare product to greatest variable and update if greater
'''

def sublist_product(sublist):
    product = 1

    for num in sublist:
        product *= num

    return product

def greatest_product(string):
    numbers = [int(char) for char in string]
    result_product = 1

    for idx in range(len(string) - 3):
        sublist = numbers[idx:idx + 4]
        current_product = sublist_product(sublist)

        if current_product > result_product:
            result_product = current_product

    return result_product


print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6