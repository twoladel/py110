'''Problem 1'''
# retrieve element 'g' from each object

lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
# lst1[2][1][3]
print(lst1[2][1][3])

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]
# lst2[1]['third'][0]
print(lst2[1]['third'][0])

lst3 = [['abc'], ['def'], {'third': ['ghi']}]
# lst3[2]['third'][0][0]
print(lst3[2]['third'][0][0])

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
# dict1['b'][1]
print(dict1['b'][1])

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
print(list(dict2['3rd'].keys())[0])
# accessed the keys, coerced view obj to a list and referenced first element
print()


'''Problem 2'''
# change value 3 to 4 in all below
lst1 = [1, [2, 3], 4]
lst1[1][1] = 4
print(lst1)

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
lst2[2] = 4
print(lst2)

dict1 = {'first': [1, 2, [3]]}
dict1['first'][2][0] = 4
print(dict1)

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
dict2['a']['a'][2] = 4
print(dict2)

print()

'''Problem 3'''
'''This one got me!'''
# given the following code what will the values of a and b be?
a = 2
b = [5, 8]
lst = [a, b] # lst == [2, [5, 8]]

lst[0] += 2 # this is changes the value in the lst object but not a which is immutable
lst[1][0] -= a # this changes the 5 at index 0 in the nested list to 3
print(a) # 2 -> a is an int and immutable 
print(b) # [3, 8]
print(lst) # [4, [1, 8]]

print()

'''Practice 4'''
# Print each Munster like so:
    # {name} is a {age}-year-old {gender}
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for key, value in munsters.items():
    print(f'{key} is a {value['age']}-year-old {value['gender']}.')