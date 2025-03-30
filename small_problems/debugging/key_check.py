'''
Why is this code raising an error. It should return the value of a key
if it exists in the

The function raises a key error on line 2 of the function definition because
the expression my_dict[key] will always return a key error if key is not
present in the dictionary. To check for membership in a dict, use the in
keyword.
'''


# def get_key_value(my_dict, key):
#     if my_dict[key]:
#         return my_dict[key]
#     else:
#         return None

# print(get_key_value({"a": 1}, "b")) 

'''Refactored code below'''

def get_key_value(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

'''Or'''

def get_key_value(my_dict, key):
    return my_dict.get(key, None)

print(get_key_value({"a": 1}, "b"))