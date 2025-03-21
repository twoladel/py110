def sequence(count, start):
    if not count:
        return []
    step = start
    if step == 0:
        return [start] * count
    return list(range(start, start * (count + 1) , step))

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True