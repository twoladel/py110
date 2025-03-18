def format_time(hour, minutes):
    return f'{hour:02d}:{minutes:02d}'


def get_minutes(num):
    while num < 0:
        num += 1440
    return num % 1440


def time_of_day(num):
    time_in_minutes = get_minutes(num)
    hour, minutes = divmod(time_in_minutes, 60)

    return format_time(hour, minutes)

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
