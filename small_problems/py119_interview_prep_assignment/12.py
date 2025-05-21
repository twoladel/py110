'''Create a function that takes a string as an argument and returns True 
if the string is a pangram, False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once. 
For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram 
since it uses every letter at least once. Note that case is irrelevant.'''

'''
P-
input string
output boolean

if alphabet is a subset of the casefolded input string
then input string is a panagram

A-
casefold input string
create alphabet variable as a set
convert input string to set
return alphabet issubset of input set
'''

def is_pangram(string):
    unique_chars = set(string.casefold())
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    return alphabet <= unique_chars

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)