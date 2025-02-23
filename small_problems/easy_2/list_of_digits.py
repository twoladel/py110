'''
input: positive int
output: list of digits that made up the arg int
explicit:

implicit:
    one digit number returns list with one digit
    maintain order as their represented in the int

D- 
convert to a str?
list

A-
create an empty list
one by one put each digit from the input number
and append it to a list
'''
def digit_list(number):
    return [int(digit) for digit in str(number)]


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
