'''Create a function that takes a list of integers as an argument. The function 
should determine the minimum integer value that can be appended to the list so 
the sum of all the elements equals the closest prime number that is greater 
than the current sum of the numbers. For example, the numbers in [1, 2, 3] 
sum to 6. The nearest prime number greater than 6 is 7. 
Thus, we can add 1 to the list to sum to 7.

Notes:

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.'''


'''
P-
input list of integers
output integer 

need an is_prime helper function
    check numbers from 2 to half the input number for even divisible
    if none then it is prime

D-

A-
Sum the input list

start a loop from the sum of the list, to the sum + 10
pass each number in the range to the is_prime funtion
when is_prime returns True
break the for loop
subtract the passed number from the sum
return that value
'''

def is_prime(num):
    for number in range(2, (num // 2) + 1):
        if num % number == 0:
            return False
    
    return True

def nearest_prime_sum(numbers):
    list_sum = sum(numbers)
    
    for number in range(list_sum + 1, list_sum + 10):
        if is_prime(number):
            break
    
    return number - list_sum




print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# # Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)