'''The commented out solution below was my original. After reviewing LS's 
solution I realized that mine is less efficient because it iterates over the 
entire dictionary instead of just the elements of the list of keys.'''
# def keep_keys(dict, key_list):
#     return {
#         key: value for key, value in dict.items()
#         if key in key_list
#         }

def keep_keys(dict, key_list):
    return {
        key: dict[key] for key in key_list
        if key in dict
        }

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True