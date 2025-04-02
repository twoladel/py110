import string

DIGIT_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine']

# def convert_word_to_digit(message):
#     for idx, digit_word in enumerate(DIGIT_WORDS):
#         if digit_word in message:
#             message = message.replace(digit_word, str(idx))
    
#     return message

# message = 'Please call me at five five five one two three four'
# print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# # Should print True

# Further exploration 

def convert_word_to_num(word):
    if word in DIGIT_WORDS:
        return str(DIGIT_WORDS.index(word))
    return word
    
def word_to_digit(phrase):
    words = phrase.split()
    new_words = []
    for word in words:
        if word[-1] in string.punctuation:
            stripped_word = word.strip(word[-1])
            digit = convert_word_to_num(stripped_word)
            combo = digit + word[-1]
            new_words.append(combo)
        else:
            new_words.append(word)

    return ' '.join(new_words)


message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True

