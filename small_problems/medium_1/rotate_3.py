'''
important numbers:
    len of sequence of digits
    one less than len is the number of rotations
    starting at the negative len idx
    first example below is:
        range(-6, -1, 1) --> range(-len(digits), -1, 1)

get len and pass number and len to the rightmost function
'''
def rotate_rightmost_digits(number, count):
    nums = list(str(number))
    last_digit = nums.pop(-count)
    nums.append(last_digit)

    return int(''.join(nums))


def max_rotation(number):
    count = len(str(number))

    for idx in range(count, 1, -1):
        number = rotate_rightmost_digits(number, idx)
    
    return number

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True