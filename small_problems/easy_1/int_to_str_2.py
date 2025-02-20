def signed_integer_to_string(number):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    sign = ''
    result_number = ''

    if number > 0:
        sign = '+'
    elif number < 0:
        number *= -1
        sign = '-'
    else:
        return '0'
    
    while number:
        number, remainder = divmod(number, 10)
        result_number = DIGITS[remainder] + result_number
        
    return sign + result_number

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True