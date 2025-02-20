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

    if not number:
        return '0'
    
    string_number = ''
    while number:
        quotient, remainder = divmod(number, 10)
        number = quotient
        string_integer = DIGITS[remainder]
        string_number += string_integer

    return string_number[::-1]

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True