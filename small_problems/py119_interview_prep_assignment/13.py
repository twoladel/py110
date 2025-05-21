'''Create a function that takes two strings as arguments and returns True 
if some portion of the characters in the first string can be rearranged to 
match the characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic 
characters. Neither string will be empty.'''

'''
P-
input: two strings
output: boolean, if all chars in 2nd string are in 1st string. Each char present,
so if 'o' appears twice, there should be two o's in the 1st string. 



D-
convert str2 to list


A-
check if char from str1 in str2
if so remove char from str2
convert str2 to list to be able to remove each char as it is checked. 
can mutate str2 while iterating str1 without running into problems. 

If the list (str2) is falsy at the end of the iteration, you should return True. 
So return not str2
'''

def unscramble(str1, str2):
    str2 = list(str2)
    for char in str1:
        if char in str2:
            idx = str2.index(char)
            str2.pop(idx)

    return not str2
            


print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)