'''Create a function that takes two string arguments and returns the number of 
times that the second string occurs in the first string. Note that overlapping 
strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.'''

'''
P-
this function tells you how many times the second arg string appears in the
first arg string.

input 2 strings
output integer, count of occurences of second string in first, not overlapping.

once letters are counted remove them from future counts
length of second string for steps in loops

would checking for membership first make it more efficient?
guard clause

D-
strings
slicing

A-
if second str not in first str 
    return 0

set counter variable to 0

for each second string length of the first string, compare to the 2nd
for start in (0, len(2nd) - 1)
    if equal, increment count
    recursive call(pass sliced string1 and same string2)

return count

'''

def count_substrings(str1, str2):
    if str2 not in str1:
        return 0
    
    step = len(str2)
    count = 0

    for start in range(0, len(str1) - (step - 1)):
        if str2 == str1[start:start + step]:
            count += 1
            count += count_substrings(str1[start+step:], str2)
            break

    return count

#Second solution - while loop
def count_substrings(str1, str2):
    if str2 not in str1:
        return 0

    length = len(str2)
    count = 0

    while str2 in str1:
        count += 1
        idx = str1.find(str2)
        str1 = str1[idx + length:]

    return count


print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)