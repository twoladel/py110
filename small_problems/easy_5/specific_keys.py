def keep_keys(dict, key_list):
    return {
        key: value for key, value in dict.items()
        if key in key_list
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