def double_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    return ''.join([char * 2 if char.lower() in consonants else char 
                    for char in string])

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")