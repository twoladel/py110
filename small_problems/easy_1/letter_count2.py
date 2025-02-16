def word_sizes(str1):
    words = {}
    str1 = str1.split()

    for word in str1:
        clean_word = ""

        for letter in word:
            if letter.isalpha():
                clean_word += letter

        words.setdefault(len(clean_word), 0)
        words[len(clean_word)] += 1

    return words

# All of these examples should print True
def run_program():
    string = 'Four score and seven.'
    print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

    string = 'Hey diddle diddle, the cat and the fiddle!'
    print(word_sizes(string) == {3: 5, 6: 3})

    string = 'Humpty Dumpty sat on a w@ll'
    print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

    string = "What's up doc?"
    print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

    print(word_sizes('') == {})

run_program()