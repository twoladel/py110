def sum_digits(number):
    return sum([int(digit) for digit in str(number)])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True