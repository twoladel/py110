def integer_to_string(number):
    DIGITS = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9'
    }

    string_number = ''
    while number:
        number, remainder = divmod(number, 10)
        string_integer = DIGITS[remainder]
        string_number += string_integer

    return string_number[::-1] or '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True