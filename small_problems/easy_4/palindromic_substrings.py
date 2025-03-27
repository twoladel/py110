def leading_substrings(word):
    return [word[0:i] for i in range(1, len(word) + 1)]

def substrings(string):
    return [substring 
            for idx in range(len(string))
            for substring in leading_substrings(string[idx:])]

def palindromes(string):
    return [
        substring for substring in substrings(string) 
        if substring == substring[::-1] and len(substring) > 1
        ]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

