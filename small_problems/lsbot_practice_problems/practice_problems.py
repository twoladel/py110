'''Write a function segment_rotate that takes two arguments: a non-negative 
integer and a segment size. The function should rotate each segment of digits 
independently and return the result as a new list. Do not mutate the list. 
If the number of digits isn't divisible by the segment size, the leftmost 
segment may be shorter than the others.'''

'''
P-
input two ints
output - new list

break a list into groups of given length and rotate each sublist
return as a new list

if length of list is not divisible by segment size, take that length from 
the right side and then make left side the remainder. 


A-
get length of list
create a variable for the result list

if len % seg_size is not 0
    len integer division seg size for how many seg sizes your getting from the right
    len % seg size for the size of the left

    use modulo return value to get the first sub list
    if int division returns more than 1
        start at modulo return value 
        get however many sublists
        extend each sublist to the result list

    else:
        get the right side and rotate it. 
else:
    nested for loop to get the sublists
    rotate the sublist one time
    extend the result list

'''
def rotate_sublist(sublist):
    return sublist[1:] + sublist[0:1]

def segment_rotate(numbers, segment_size):
    length = len(numbers)
    rotated_list = []

    if length % segment_size == 0:
        for start in range(0, len(numbers), segment_size):
            sublist = rotate_sublist(numbers[start:start + segment_size])
            rotated_list.extend(sublist)
        return rotated_list
    else:
        segment_count = length // segment_size
        left_side_segment_size = length % segment_size
        left_sublist = numbers[:left_side_segment_size]
        rotated_list.extend(rotate_sublist(left_sublist))

        if segment_count > 1:
            for start in range(left_side_segment_size, len(numbers), segment_size):
                sublist = rotate_sublist(numbers[start:start+segment_size])
                rotated_list.extend(sublist)
        else:
            right_sublist = numbers[left_side_segment_size:]
            rotated_list.extend(rotate_sublist(right_sublist))
            
        return rotated_list


# Examples:
# print(segment_rotate([1, 2, 3, 4, 5, 6], 2) == [2, 1, 4, 3, 6, 5])  
# print(segment_rotate([1, 2, 3, 4, 5, 6], 3) == [2, 3, 1, 5, 6, 4])  
# print(segment_rotate([1, 2, 3, 4, 5, 6], 4) == [2, 1, 4, 5, 6, 3])  
# print(segment_rotate([1, 2, 3], 5) == [2, 3, 1])            
# print(segment_rotate([1, 2, 3, 4, 5, 6, 7], 2) == [1, 3, 2, 5, 4, 7, 6])  


'''Create a function called balanced_chars that returns the count of distinct case-insensitive alphabetic characters that occur exactly the same number of times in the input string (at least twice each) You may assume that any char occurences greater than 1 are all the same count.
'''
'''
P-
input string
output integer

D-
dict / map
A-
create a dict of char counts
    confirm char isalphnum()
    key will be char
    value will be occurences
list comp to iterate of dict values and store any that are more than one

return the length of that list 

15 minutes to write PEDAC
'''

# def balanced_chars(string):
#     string = string.casefold()
#     char_counts = {}
#     for char in string:
#         if char.isalnum():
#             char_counts.setdefault(char, 0)
#             char_counts[char] += 1

#     repeated_char_counts = [
#         value 
#         for value in char_counts.values()
#         if value > 1
#         ]
#     return len(repeated_char_counts)
    

# # Examples:
# print(balanced_chars('aabccdee') == 3)   
# print(balanced_chars('abbbcddd') == 2)        
# print(balanced_chars('ABabCDcd') == 4)      
# print(balanced_chars('hello') == 1)            
# print(balanced_chars('python') == 0)           



'''Create a function called consecutive_duplicates that returns the number of distinct alphabetic characters and numeric digits that appear at least twice consecutively in the input string. Ignore case when counting alphabetic characters.'''
'''
counter can increment anytime you find consecutive, don't need to count occurences
if it is also equal to two previous continue
'''

# def consecutive_duplicates(string):
#     pass

# # Examples:
# print(consecutive_duplicates('aabbc12223') == 3) 
# print(consecutive_duplicates('aBbCcDa') == 2) 
# print(consecutive_duplicates('hello11world') == 2) 
# print(consecutive_duplicates('programming') == 1)   
# print(consecutive_duplicates('python3.9') == 0)    


'''Create a function that takes a list of integers as an argument and returns a list of all possible products formed by multiplying each integer with each subsequent even integer in the list.
For example, if the input list is [1, 2, 3], you should calculate products by multiplying 1 with 2. The resulting list would be [2].
If the input list has fewer than 2 elements, return an empty list.'''#Wednesday

'''
P-
input list of integers
output list of products 

fewer than two elements, return empty list

D- 
lists
loops

A-
if len input list is less than 2, return an empty list

create empty result list

for number in list
    multiply it by each subsequent number in the list
    nested loop
    start is outer loop (end one earlier than a normal loop)
    stop is inner loop (stop should begin at start plus 1)
    multiply element at start by element at each stop
    add each product to the result list
return result list
'''

def subarray_products(list): # Wednesday 
    result = []
    if len(list) < 2:
        return result
    
    return [list[start] * list[stop]
        for start in range(len(list) - 1)
        for stop in range(start + 1, len(list))
        if list[stop] % 2 == 0]


# Examples, all should print True
# print(subarray_products([1, 2, 4, 6]) == [2, 4, 6, 8, 12, 24])
# print(subarray_products([2, 5, 10]) == [20, 50])
# print(subarray_products([7]) == [])
# print(subarray_products([]) == [])
# print(subarray_products([2, 3, 1, 6, 7, 8]) == [12, 16, 18, 24, 6, 8, 48, 56])


def word_indices(string):
    word_lst = string.split()
    result = {}
    char_count = 0

    for word in word_lst:
        if word in result:
            result[word].append(char_count)
        else:
            result[word] = [char_count]
        
        char_count += (len(word) + 1)
    
    return result

# def word_indices(string):
#     words = string.split()
#     result = {}

#     for word in words:
#         if word not in result:
#             result[word] = []
#             occurences = string.count(word)
#             start = 0
#             for _ in range(occurences):
#                 idx = string.index(word, start)
#                 result[word].append(idx)
#                 start = idx + 1
#     return result

# print(word_indices("the fox jumps over the long brown fence"))


# Create a function that converts a string into a "run-length encoding".
# Each sequence of identical characters should be replaced with the character
# followed by the count of consecutive occurrences. If a character appears
# only once, just include the character without a count.

'''
P-
input string
output new string with chars and count of consecutive occurences, no count if only 1 

D-

A-
create a result string
count set to 1

iterate over the input string
for each char
    iterate till we find a different char
    if index == len(str) - 1 or char is not equal to next char
        add the char to new string
        if count is greater than 1
            add the count to the new string
            count resets to 1
    else
        count increments by one
        
'''
def run_length_encode(string):
    result = ''
    count = 1

    for idx, char in enumerate(string):
        if idx == len(string) - 1 or char != string[idx + 1]:
            result += char
            if count > 1:
                result += str(count)
                count = 1
        else:
            count += 1
    return result


# print(run_length_encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB") == "W12BW12B3W24B")
# print(run_length_encode("aabcccccaaa") == "a2bc5a3")
# print(run_length_encode("abcdef") == "abcdef")
# print(run_length_encode("") == "")
# print(run_length_encode("aaaaaaaaaa") == "a10")

# 5/10/2025

'''Create a function that takes a list of integers and returns a new list where each element is the product of all numbers in the original list except the number at that position. You should not use division in your solution.'''

'''
P-
input list of ints
output: list of ints that are products of all numbers except the current position.

one element returns a list with the value 1.

D-
sublists

A-
list comp?

create an empty result list
for current index
    get values at all other indexes and multiply them together
    create a sublist with slicing 
    pass to a helper funciton
    helper iterates and multitplies and returns product
    returned product is appended
return result list

for idx in range(len(list))
    sublist = []
    if idx == len(list) - 1
        sublist = list[:idx]
    else:
        sublist = list[:idx] + list[idx + 1:]

    result.append(get product(sublist))

helper:
product = 1
for num in sublist:
    product *= num
return product

'''

def product_except_self(numbers):
    pass

 # Examples:
# print(product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6])
# print(product_except_self([5, 3, 4, 2, 6]) == [144, 240, 180, 360, 120])
# print(product_except_self([10]) == [1])
# print(product_except_self([11, 0, 7]) == [0, 77, 0])


'''Create a function that takes a list of words and groups anagrams together. An anagram is a word formed by rearranging the letters of another word. The function should return a list of lists, where each inner list contains a group of anagrams. Don't mutate the original list'''

'''
P-
input list of words
output: nested list with anagrams grouped togehter

empty list returns empty list

D-
sets to compare words
lists
append

A-
the first word will go into its own nested list
then we need to compare each subsequent word to the first word in the first list
    use sets to compare for equality
    if not equal append to a new nested list
    if there are more than one nested list have to check it too. 

create a nested list, with the first word of input list as the only element.

start iterating thru the rest of the list starting at index 1
for each word
    coerce to a set
    compare with element in each nested list coerced to a set
    This is another iteration
    if equal
        append to that nested list
    else
        create a new nested list with this word as an element

'''

# def in_nested(word, nested_list):
#     for sublist in nested_list:
#         if word in sublist:
#             return True
#     return False

# def group_anagrams(words):
#     if not words:
#         return []
#     nested_words = [[words[0]]]

#     for idx in range(1, len(words)):
#         chars = set(words[idx])

#         for nested in nested_words:
#             if set(nested[0]) == chars:
#                 nested.append(words[idx])
#                 break
    
#         if not in_nested(words[idx], nested_words):
#             nested_words.append([words[idx]])
                
#     return nested_words

# recreate without saving words with no anagrams, like bat below
def group_anagrams(lst):
    anagrams = {}

    for word in lst:
        key = ''.join(sorted(word))
        
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
        
    return list(anagrams.values())

# Examples:
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
print(group_anagrams(["listen", "silent", "enlist", "hello", "world"]) == [["listen", "silent", "enlist"], ["hello"], ["world"]])
print(group_anagrams([]) == [])



# Create a function that takes a nested list (a list of lists) as an argument.
# The function should return a new list where each element is a tuple containing:    
# •   The sum of all numbers in the sublist
# •   The sublist itself with all even numbers replaced by the string "even" 

'''
P-
input: nested list, nested lists contain integers
output: nested list of tuples, each tuple contains an int (sum of the sublist) and the original sublist with even numbers transformed to the string 'even'

empty nested list, returning 0 sum and an empty sublist

D-
lists
tuples

A-

iterate over the input list
for each sublist
    do stuff
    sum the sublist
    iterate over the sublist
        create a new empty sublist
        if the number is even
            append the word even
        else
            append the number
        
    build a tuple with the sum and new sublist
    append the tuple to the new result list 


'''

def transform_lists(nested_list):
    # result = []
    return [
        (sum(sublist), 
        ['even' if number % 2 == 0 else number for number in sublist ])
        for sublist in nested_list
    ]
    # for sublist in nested_list:
    #     sublist_sum = sum(sublist)
    #     new_sublist = []
    #     for number in sublist:
    #         if number % 2 == 0:
    #             new_sublist.append('even')
    #         else:
    #             new_sublist.append(number)
    #     result.append((sublist_sum, new_sublist))
    # return result

print(transform_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [(6, [1, "even", 3]), (15, ["even", 5, "even"]), (24, [7, "even", 9])])
print(transform_lists([[10, 20], [30, 40, 50]]) == [(30, ["even", "even"]), (120, ["even", "even", "even"])])
print(transform_lists([[1, 3], [5, 7, 9]]) == [(4, [1, 3]), (21, [5, 7, 9])])
print(transform_lists([[]]) == [(0, [])])



