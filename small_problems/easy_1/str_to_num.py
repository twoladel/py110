'''
P-
input: string of digits
output: int repr of those digits
explicit:
    no constructor functions
    manipulate chars in the string to create number
implicit:
    places grow by 10 (1, 10, 100, 1000)
    positive int

D-
helper dict of digits and str version

A-
create constant dict of digits: str as keys and ints as values
create a num variable to hold the result
convert each digit to a number and build the number
    for digit in string number
        grab the int_digit from the dict
        add the digit to the number
            add digit to product of 10 * the current result
    return result
'''
def string_to_integer(str_num):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    result = 0
    for digit in str_num:
        digit = DIGITS[digit]
        result = digit + (result * 10)
    return result

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True