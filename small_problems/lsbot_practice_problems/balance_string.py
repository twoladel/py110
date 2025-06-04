'''Problem: Finding Balanced Substrings
Create a function that takes a string consisting only of the characters 
'(' and ')' as an argument. 
The function should return the length of the longest balanced substring.

A balanced substring is one where:
1.  Every opening parenthesis '(' has a matching closing parenthesis ')'
2.  The parentheses are properly nested (a closing parenthesis never appears 
before its matching opening parenthesis)'''

'''
P-
input string of parentheses chars
output - integer representing the length of longest balanced substring

E-
D-
nested loops
start and stop indexes to track
substrings
helper function to check for balance

A-
set a length variable to zero

iterate over the string 
    check each possible substring for balance
    if balanced 
        get length 
    if greater than current length
        update length
    if length is longer than remaining iteratiions break?


if substring starts with ')' automatically not balanced
    continue
if substring starts with '(' 
    iterate the stop index
    send to the is_balanced function


is_balanced algorithm
take a string 
output a boolean

counter for open paren
counter for close paren

count while iterating
check if close is greater than open
if yes
    return False
if its an open
    increment open
if its a close
    increment close

after iteration complete if counter not equal 
    return False
else
    return True
'''

def is_balanced(string):
    open_paren = 0
    close_paren = 0

    for char in string:
        if close_paren > open_paren:
            return False
        
        if char == '(':
            open_paren += 1
        else:
            close_paren += 1

    if open_paren == close_paren:
        return True
    else:
        return False

def longest_balanced(string):
    substr_length = 0

    for start in range(len(string)):
        if len(string) - start < substr_length:
            break

        if string[start] == ')':
            continue

        for stop in range(start + 1, len(string) + 1):
            if is_balanced(string[start:stop]):
                current_len = len(string[start:stop])
                if current_len > substr_length:
                    substr_length = current_len

    return substr_length
            


print(longest_balanced('(()') == 2)           # The balanced substring is "()"
print(longest_balanced(')()()(') == 4)        # The balanced substring is "()()"
print(longest_balanced('(()())') == 6)        # The whole string is balanced
print(longest_balanced('))((') == 0)          # No balanced substrings
print(longest_balanced('())(())(())') == 8)   # The balanced substring is "(())()"6
