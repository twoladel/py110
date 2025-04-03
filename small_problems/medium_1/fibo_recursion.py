import time

start_time = time.perf_counter()

def fibonacci(num):
    if num < 3: # base case
        return 1
    
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")