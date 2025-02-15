def is_palindrome(str1):
    return str1 == str1[::-1]


def is_real_palindrome(s):
    s = s.casefold()
    s = ''.join([char for char in s if char.isalnum()])
    return is_palindrome(s)

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True