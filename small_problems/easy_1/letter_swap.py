'''First function is my first attempt at this problem. Commented out below is 
a second attempt in which I recreated LS's solution to ensure I understood it.'''

def swap(s):
    if len(s) == 1:
        return s
    s = s.split()
    new_words = []
    for word in s:
        chars = list(word)
        char = chars.pop()
        chars.insert(0, char)

        if len(word) > 2:
            char = chars.pop(1)
            chars.append(char)

        new_words.append("".join(chars))

    new_s = " ".join(new_words)

    return new_s

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

# def swap(s):
#     words_list = s.split()
#     for idx in range(len(words_list)):
#         words_list[idx] = swap_chars(words_list[idx])

#     return ' '.join(words_list)

# def swap_chars(word):
#     if len(word) == 1:
#         return word
    
#     return word[-1] + word[1:-1] + word[0]
        
# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True