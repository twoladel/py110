'''Create a function that takes two strings as arguments and returns True 
if some portion of the characters in the first string can be rearranged to 
match the characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic 
characters. Neither string will be empty.'''

'''
P-

'''

def unscramble(str1, str2):
    str2 = list(str2)
    for char in str1:
        if char in str2:
            idx = str2.index(char)
            str2.pop(idx)

    return not bool(str2)
            


print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)