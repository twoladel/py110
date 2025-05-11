'''Create a function that takes a string argument and returns a copy of 
the string with every second character in every third word converted 
to uppercase. Other characters should remain the same.'''

'''
P-
input string
output: copy of string with every 2nd char(every odd idx) in every 3rd word
coverted to uppercase.

for every third word
    uppercase every char at an odd index

D-
list of words
build new strings
A-
make list of words

for every 3rd word
    create new_word_variable
    for each char
        if char's index is odd
            concatenate upper char
        else
            concatenate char
    
    update list with modified word
join list back to string
return
'''

def to_weird_case(string):
    words = string.split()

    for idx in range(2, len(words), 3):
        modded_word = ''
        for index, char in enumerate(words[idx]):
            if index % 2 != 0:
                modded_word += char.upper()
            else:
                modded_word += char

        words[idx] = modded_word

    return ' '.join(words)


original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)