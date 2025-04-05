import time

start_time = time.perf_counter()

MAX_FEATURED = 9876543201

def start_at_odd_mulitple_of_seven(number):
    if number % 7 != 0:
        start = number + 7 - (number % 7)
    else:
        start = number + 7

    if start % 2 == 0:
        start += 7

    return start

def next_featured(number):
    if number >= MAX_FEATURED:
        return 'There is no possible number that fulfills those requirements.'

    start = start_at_odd_mulitple_of_seven(number)

    for num in range(start, MAX_FEATURED + 1, 14):
        if len(str(num)) == len(set(str(num))):
            return num


print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

end_time = time.perf_counter()
elapsed = end_time - start_time
print(f'Runtime: {elapsed:.4f}')