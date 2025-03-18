'''
P- convert time in minutes to 24hr time.
input: is an int, positive or negative
output: string in 24 hour format
Explicit:
    Any integer input
    No datetime module
    negative input is count down from midnight
    positive is count up to midnight
Implicit:
    0 is 00:00
    1440 minutes in a 24 hour day
    24 increments of 60
    1439 = 23:59

E-
Will take times that are outside the 24 hour window and will need to reset

D- 
intergers and formatted strings
pad zeros functions?

A-
Adjust input to an int between 0 and 1440
Find what time of day that is
    what hour divide minutes by 60
    multiply remainder by 60 for the minutes
    divmod function will work
Pad zeros for formatting
return f-string with values interpolated
'''
def pad_zeros(num):
    str_num = str(num)
    if len(str_num) == 1:
        return '0' + str_num

    return str_num


def get_minutes(num):
    while num > 1440:
        num -= 1440

    while num < 0:
        num += 1440
    return num


def time_of_day(num):
    time_in_minutes = get_minutes(num)
    hour, minutes = divmod(time_in_minutes, 60)

    hour = pad_zeros(hour)
    minutes = pad_zeros(minutes)

    return f'{hour}:{minutes}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
