def after_midnight(time_str):
    hour = int(time_str[0:2])
    minutes = int(time_str[3:])
    if hour == 24:
        return 0

    return (hour * 60) + minutes

def before_midnight(time_str):
    hour = int(time_str[0:2])
    minutes = int(time_str[3:])
    if hour == 0:
        return 0
    
    return ((24 - hour) * 60) - minutes

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True