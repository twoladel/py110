from datetime import date

def friday_the_13ths(year):
    fridays = 0

    for month in range(1, 13):
        if date(year, month, 13).weekday() == 4:
            fridays += 1

    return fridays

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True