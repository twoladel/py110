def count_adjacent_consonants(string):
    
    string = ''.join(string.split())
    max_count = 0
    temp_string = ''

    for char in string:
        if char not in 'aeiou':
            temp_string += char
            if len(temp_string) > max_count and len(temp_string) > 1:
                max_count = len(temp_string)
        else:
            temp_string = ''

    return max_count

def sort_by_consonant_count(strings):
    strings.sort(key=count_adjacent_consonants, reverse=True)
    return strings

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']