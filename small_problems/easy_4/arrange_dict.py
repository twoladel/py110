def order_by_value(dict):
    pairs = sorted(dict.items(), key=sort_key)
    return [key for key, value in pairs]

def sort_key(pair):
    return pair[1]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)   #True