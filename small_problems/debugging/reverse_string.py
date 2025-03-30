'''Explain the bug and provide refactored code.'''

def reverse_string(string):
    for char in string:
        string = char + string

    return string

print(reverse_string("hello") == "olleh") # False

'''The bug is due to variable scope. The string parameter is referencing
the string object that is passed to the function. So line 5 is concatanating
additional characters onto the string by reassigning the value of string to the
expression char + string. We need to initialize a variable to an empty string
to store the reversed result.'''

def reverse_string(string):
    result = ''
    for char in string:
        result = char + result

    return result

print(reverse_string("hello") == "olleh") # True