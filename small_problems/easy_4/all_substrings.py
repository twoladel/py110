# def substrings(string):
#     result = [string[i:idx] for i in range(len(string))
#                             for idx in range(i + 1, len(string)+ 1)]
#     return result

def leading_substrings(word):
    return [word[0:i] for i in range(1, len(word) + 1)]

def substrings(string):
    result = []
    for idx in range(len(string)):
        result.extend(leading_substrings(string[idx:]))

    return result

# expected_result = [
#     "a", "ab", "abc", "abcd", "abcde",
#     "b", "bc", "bcd", "bcde",
#     "c", "cd", "cde",
#     "d", "de",
#     "e",
# ]

expected_result = [
    'e', 'eb', 'ebc',
    'b', 'bc',
    'c'
]

print(substrings('ebc') == expected_result)


# print(substrings('abcde') == expected_result)  # True


# print(substrings('abcde'))