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

def remove_vowels(string_list):
    return [no_vowels(string) for string in string_list]

def no_vowels(string):
    new_str = ''
    for char in string:
        if char.casefold() not in 'aeiou':
            new_str += char
    return new_str


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