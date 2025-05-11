'''Create a function that takes a string argument and returns the character 
that occurs most often in the string. If there are multiple characters with 
the same greatest frequency, return the one that appears first in the string. 
When counting characters, 
consider uppercase and lowercase versions to be the same.'''

'''
P-
input string
output one char (string) with highest count

casefold the string
if two have high count, return first

D-
dict

A-
create an empty dict
casefold the string

compile char counts into a dict
for char in string:
    setdefault
    increment count


get key with max value
list comp: key for key, value in dict.items if value == max(dict.values())

return keys[0]
'''


def most_common_char(string):
    char_counts = {}
    string = string.casefold()

    for char in string:
        char_counts.setdefault(char, 0)
        char_counts[char] += 1

    max_count_keys = [
        key for key, value in char_counts.items()
        if value == max(char_counts.values())
    ]
    print(max_count_keys)
    return max_count_keys[0]

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')