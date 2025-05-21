'''Create a function that takes a nonempty string as an argument and returns 
a tuple consisting of a string and an integer. If we call the string 
argument s, the string component of the returned tuple t, 
and the integer component of the tuple k, then s, t, and k must be related to 
each other such that s == t * k. The values of t and k should be the shortest 
possible substring and the largest possible repeat count that satisfies this 
equation.

You may assume that the string argument consists entirely of 
lowercase alphabetic letters.'''

'''
P-
input string
output tuple consisting of substring and repetitions of substring that 
equal the input string. 

Find the smallest repeating substring that will rebuild the input string

the length of the substring times the repetion equals the length of the string

the result substring will always include the first char

if each iteration checks a longer substring and you divide len of string by
len of substring to get mulitplier
multiply current substring by multiplier and compare to input

when they are equal
break the loop
return tuple with substring and multiplier

D-

A-
get length of input string

for each stop index (start at 1 and end at length of string)
    get the substring slice length which is the current stop index
    so string len / stop index
    multiple slice by multiplier
    check against input
    break on a match
'''

def repeated_substring(string):
    input_length = len(string)

    for stop in range(1, input_length + 1):
        multiplier = int(input_length / stop)
        substring = string[:stop]

        if multiplier * substring == string:
            break
    return substring, multiplier

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))