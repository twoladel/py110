# PEDAC practice - assignment 9 

# input: string
# output: list of substrings (new object)
# rules:
# explicit requirements:
    # function name: palindrome_substrings
    # return only substrings that are palindromes
    # case sensitive: mom, but not Mom
    # must be two or more chars
# implicit requirements:
    # none should return empty list
    # empty string should return empty list
# questions:
    # will strings all be one 'word'?
    # will punctuation show up? if so, how do we handle it?

# Data struct: list

# Algorithm - My first run at the algorithm:
    # Declare result variable and initialize as an empty list
    # find all substrings of two or more chars 
    # *LS suggests creating a list of all substrings in string
    # then iterating over the list to check for palindromes*
        # start at first char
        # incrementaly compare from second char to end of string looking for substring palindromes
        # move to second char and do the same
        # last check should be second to last char
        # use a for loop to iterate over the string
        # use slicing notation to get each substring for each char in string
    # check each substring with an is_palindrome function
    # if true append to list
    # return list

def palindrome_substrings(str1):
    palindrome_subs = []

    # extract all substrings of 2 or more chars from str1 into a list
    substrs_list = substrings(str1)

    for sub in substrs_list:
        if is_palindrome(sub):
            palindrome_subs.append(sub)

    return palindrome_subs


def is_palindrome(substring):
    return substring == substring[::-1]

# Used LS's informal pseudocode to build function
'''- Create an empty list, `result`, for the required substrings.
- Initialize a `start_index` variable to 0 for the first character of
  the substring.
- Iterate over the string from `start_index` to length of string - 2.
    - Initialize a `num_chars` variable to `2` for the initial
      substring length.
    - Iterate from `num_chars` to length of string - `start_index`:
        - Extract substring of length `num_chars` from `string`
          starting at `start_index`.
        - Append the extracted substring to `result`.
        - Increment `num_chars` by `1`.
    - End of inner loop.
    - Increment `start_index` by `1`.
- End of outer loop.
- Return the `result` list.'''


def substrings(string):
    result_lst = []
    start_index = 0

    while start_index <= len(string) - 2:
        num_chars = 2
        while num_chars <= len(string) - start_index:
            substring = string[start_index:start_index + num_chars]
            result_lst.append(substring)
            num_chars += 1

        start_index += 1

    return result_lst

# Test cases
print(palindrome_substrings("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings(""))           # []
print(palindrome_substrings("repaper"))
# ['repaper', 'epape', 'pap']

print(palindrome_substrings("supercalifragilisticexpialidocious"))
# ["ili"]