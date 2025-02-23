'''
P-
input: list
output: each element of the list with number of occurences in list
Explicit:
    case sensitive
Implicit:
    use => in f-string output

D- 
input: list
output: string formatted
intermediate: dict list of tuples?

A-
create an empty dict
iterate over list to get counts of occurences
add each key:value to a dict
iterate over dict to print the output strings
Can I just print each from within the loop? no
'''

def count_occurrences(lst):
    occurences_dict = {}

    for item in lst:
        occurences_dict[item] = occurences_dict.get(item, 0) + 1

    for key, value in occurences_dict.items():
        print(f'{key} => {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2