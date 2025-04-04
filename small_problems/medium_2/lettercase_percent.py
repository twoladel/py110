def percentages(count, length):
    return f"{(count / length) * 100:.2f}"

def letter_percentages(string):

    length = len(string)
    upper_count = 0
    lower_count = 0
    neither_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        else:
            neither_count += 1
    
    return {'lowercase': percentages(lower_count, length),
    'uppercase': percentages(upper_count, length),
    'neither': percentages(neither_count, length)}

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)