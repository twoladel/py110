# def remove_vowels(string_lst): # Initial solution
#     result = []
#     for string in string_lst:
#         new_string = ''
#         for char in string:
#             if char.casefold() not in 'aeiou':
#                 new_string += char
#         result.append(new_string)
#     return result

'''Refactored as a comprehension with a helper function.'''

VOWELS = 'AEIOUaeiou'

def remove_vowels(string_list):
    return [no_vowels(string) for string in string_list]

def no_vowels(string):
    return ''.join([char for char in string if char not in VOWELS])
    


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True