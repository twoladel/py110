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
        