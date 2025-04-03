def fibonacci(num):
    if num < 3:
        return 1
    
    f1 = 1
    f2 = 1

    for _ in range(3, num + 1):
        n = f1 + f2
        f1 = f2
        f2 = n

    return n

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True