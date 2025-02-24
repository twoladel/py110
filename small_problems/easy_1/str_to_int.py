def string_to_signed_integer(str_num):

    if str_num.startswith('+'):
        str_num = str_num.lstrip('+')
        return string_to_integer(str_num)
    elif str_num.startswith('-'):
        str_num = str_num.lstrip('-')
        return string_to_integer(str_num) * -1
    else:
        return string_to_integer(str_num)
        

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
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True