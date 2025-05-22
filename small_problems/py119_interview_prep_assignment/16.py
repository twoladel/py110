'''Create a function that returns the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in the 
input string. You may assume that the input string contains only alphanumeric 
characters.'''

'''
P-
input: string
output: integer, count of distinct chars (case insensitive) that occur > 1

we need to casefold the string for case insensitivity

D-
dictionary for char counts

A-
create an empty dict
casefold the input string

iterate over the string to build the char count dict
for char in string
    create a dict entry or if one exists increment the value associated with
    that key

return the length of a list containing char count values greater than 1

'''

def distinct_multiples(string):
    char_counts = {}
    string = string.casefold()

    for char in string:
        char_counts.setdefault(char, 0)
        char_counts[char] += 1
    
    return len([
        key for key, value in char_counts.items()
        if value > 1])
    

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5