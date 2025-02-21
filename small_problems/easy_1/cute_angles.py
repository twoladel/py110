'''
P & E-
input: float between 0 and 360 (repr an angle)
output: string (repr an angle) in degrees, minutes, and seconds
Explicit:
    - each of d,m, and s are followed by symbols (degree symbol, ', ")
    - 60 minutes in a degree, 60 seconds in a minute
    - 
Implicit:
    - need escape char for " after seconds in output string
    - 0 input should return 0, 00, 00
    - 360 input should return either 360, 00, 00 or 0, 00, 00
    - if int input, minutes and seconds will be 00
    - minutes and seconds must always contain two digits
    - convert each degree, minute, second to int before interpolating
    - whole number part of input float is the degree

D-
floats, ints, and strings
f-strings for output

A-
Need quotients and integers (divmod?)
Initialize DEGREE constant given in problem description
Extract whole number from front of float assign to degree variable 
    - divide by 1
Take remainder, multiply by 60 and assign to minute variable 
    - two steps above is divmod into two variables
Take remainder, multiply by 60 and assign to second variable
convert minutes and seconds to strings, check if they have two digits or one
    - if only one digit, prepend a 0 to front of string
return f-string with variables interpolated into appropriate positions
convert to int before return?

'''
def ensure_two_digits(num):
    str_num = str(int(num))
    if len(str_num) == 1:
        return '0' + str_num
    
    return str_num


def dms(number):
    DEGREE = "\u00B0"

    if number < 0 or number > 360:
        number = sanitize_number(number)

    degrees, remainder = divmod(number, 1)
    minutes = remainder * 60
    seconds = (minutes % 1) * 60

    minutes = ensure_two_digits(minutes)
    seconds = ensure_two_digits(seconds)

    return f"{int(degrees)}{DEGREE}{minutes}'{seconds}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

'''Refactored for Further Exploration piece.
P-
input: any negative or positive number
output: same as above

A-
additional math steps
if outside the range of 0 - 360
helper function:
    if < 0
        get quotient of input divided by -360
        add input to 360 * quotient
        Now we have a negative number between -360 and 0
        subtract that number from 360
        return number
    if > 360
        get quotient of input divided by 360
        subtract 360 * quotient from input
        return number
'''
def sanitize_number(number):
    if number < 0:
        quotient = number // -360
        number += (360 * quotient) + 360
        return number
    if number > 360:
        quotient = number // 360
        return number - (360 * quotient)
    
print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"