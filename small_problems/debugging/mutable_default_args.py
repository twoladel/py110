'''
The function is continuing to mutate the original list instead of appending
to a new empty list each time.

Default function args can be mutable if they are of a mutable type. We must
initialize the default empty list inside the function.

Played with the mutability of default dicts below.
'''

def append_to_list(value):
    lst=[]
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2))
print(append_to_list(2) == [2])
print(append_to_list(3))

def add_to_dict(key, value, my_dict={}):
    my_dict[key] = value
    return my_dict

print(add_to_dict(1, '1') == {1: '1'}) # True
print(add_to_dict(2, '2')) # {1: '1', 2: '2'}
new_dict = add_to_dict(2, '3')
print(add_to_dict(3, '4')) # {1: '1', 2: '3', 3: '4'}
print(new_dict)
add_to_dict(3, '3', new_dict)
print(new_dict) # {1: '1', 2: '3', 3: '3'}
