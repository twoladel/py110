# '''Problem 1'''
# # print the total age of all male munsters
# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }
# print(sum([munster['age'] for munster in munsters.values()
#                           if munster['gender'] == 'male']))

# print()

# '''Problem 2'''
# # return new list with same structure but elements in nested lists sorted in ascending order
# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# print([sorted(list) for list in lst])
# print()

# '''Problem 3'''
# # return new list with same struct but sorted in ascending as strings
# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# # use keyword arg to call str()
# print([sorted(list, key=str) for list in lst])
# print()

# '''Problem 4'''
# # Dict comp: first element is key, second element is value
# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]

# dict1 = {sublist[0]: sublist[1] for sublist in lst}
# print(dict1 == # Pretty printed for clarity
# {
#     'a': 1,
#     'b': 'two',
#     'sea': {'c': 3},
#     'D': ['a', 'b', 'c']
# })
# print()

# '''Problem 5'''
# # Sort the list, so the sublists are ordered by the sum of the odd numbers they contain
# # Don't mutate the original list
# # Identity transformation and selection based off sum of odd nums
# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

# def sum_odds(nums):
#     return sum([num for num in nums if num % 2 == 1])
# sorted_nests = sorted(lst, key=sum_odds)
# print(sorted_nests)
# print()

# '''Problem 6'''
# # same struct, new list, increment dict values by 1
# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# def increment_values(dict):
#     return {key: value + 1 for key, value in dict.items()}

# new_list = [increment_values(dict) for dict in lst]

# print(new_list)
# print()
# # as a single comprehension:
# '''new_list = [{key: value + 1 for key, value in dictionary.items()}
#                             for dictionary in lst]'''

# '''Problem 7'''
# # return same struct list, with only multipliers of 3 in nested lists, empty if necessary
# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# new_list = [[num for num in list if num % 3 == 0]
#                 for list in lst]
# print(new_list)
# print()
# # more readable solution with helper function
# '''def divisible_by_3(sublist):
#     return [num for num in sublist if num % 3 == 0]

# new_list = [divisible_by_3(sublist) for sublist in lst]
# print(new_list)'''

# '''Problem 8'''
# # Return a list of values from inner dicts
#     # colors from fruits and should be capitalized
#     # size from vegetables and should be all caps
#     # two diff filters and two diff transformations
# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }

# def transform_value(food):
#     if food['type'] == 'vegetable':
#         return food['size'].upper()
#     else:
#         return [color.capitalize() for color in food['colors']]

# print([transform_value(food) for food in dict1.values()])
# print()

# '''Problem 9'''
# # Return a list of only the dicts that contain even numbers
# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]
# # expected output: [{'e': [8], 'f': [6, 10]}]

# '''
# P-
# input: list of dicts
# output: list of dicts, but only dicts that have all even numbers in value lists
# Explicit: must return a new list, not mutated
# Implicit: dicts within list can be varying sizes

# A- 
# filter out the dicts containing odd numbers with a helper function
# user helper function return value for filtering (as if condition)
# '''
# def filter_odds(dict):
#     for list in dict.values():
#         for num in list: # LS solution used all() w/ list comprehension here.
#             if num % 2 == 1:
#                 return
#     return dict
    
# new_list = [dict for dict in lst if filter_odds(dict)]
# print(new_list)
# print()

# '''Problem 10'''
# # This solution is LS's - my original solution is uuid() below
# import random
# def generate_uuid():
#     hex_chars = '0123456789abcdef'
#     sections = [8, 4, 4, 4, 12]
#     uuid = []

#     for section in sections:
#         chars = [random.choice(hex_chars) for _ in range(section)]
#         uuid.append(''.join(chars))

#     return '-'.join(uuid)

# print(generate_uuid())

# def uuid():
#     hex_chars = '0123456789abcdef'
#     elements = random.choices(hex_chars, k=32)
#     return (f"{''.join(elements[:8])}-{''.join(elements[8:12])}-"
#     f"{''.join(elements[12:16])}-{''.join(elements[16:20])}-"
#     f"{''.join(elements[20:])}")

# print(uuid())           

'''Problem 11'''


