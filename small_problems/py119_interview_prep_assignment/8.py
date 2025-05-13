'''Create a function that takes a non-empty string as an argument. The string 
consists entirely of lowercase alphabetic characters. The function should 
return the length of the longest vowel substring. 

The vowels of interest are "a", "e", "i", "o", and "u".'''

'''
P-
input string
output integer, that is length of longest vowel substring

1 is the shortest length
no empty strings to worry about

D-
substrings
slicing

A-
current_longest variable
counter variable

for each letter
if it is a vowel
    increment count
    check count against current longest
    update if longer
if it is not a vowel
    reset count to zero
    continue
'''
def longest_vowel_substring(string):
    longest_sub = 0
    vowel_count = 0

    vowels = 'aeiou'

    for char in string:
        if char in vowels:
            vowel_count += 1
            if vowel_count > longest_sub:
                longest_sub = vowel_count
        else:
            vowel_count = 0
    
    return longest_sub


print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)