def running_total(lst):
    totals = []
    total = 0

    for num in lst:
        total += num
        totals.append(total)
        
    return totals


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True