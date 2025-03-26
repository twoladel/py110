'''I started doing a match/case solution. Once I tested it with fewer numbers 
and confirmed it worked. I looked at the LS solution and saw they used a list
of the words with each word at the index it represented. Implemented that
further below.'''
# def word_key(number):
#     match number:
#         case 0:
#             return 'zero'
#         case 1:
#             return 'one'
#         case 2:
#             return 'two'
#         case 3: 
#             return 'three'
#         case 4:
#             return 'four'
        
# def alphabetic_number_sort(numbers):
#     return sorted(numbers, key=word_key)
        
# my_list = [0, 1, 2, 3, 4]
# expected_result = [4, 1, 3, 2, 0]

# print(alphabetic_number_sort(my_list) == expected_result)

NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
           'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
           'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

def word_key(num):
    return NUMBERS[num]

def alphabetic_number_sort(numbers):
    return sorted(numbers, key=word_key)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)  # True