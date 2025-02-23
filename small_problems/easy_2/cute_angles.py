def ensure_two_digits(num):
    str_num = str(int(num))
    if len(str_num) == 1:
        return '0' + str_num
    
    return str_num


def dms(number):
    DEGREE = "\u00B0"

    if number < 0 or number > 360:
        number %= 360

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

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"

print(dms(-740)) # 340
print(dms(-1200)) # 240