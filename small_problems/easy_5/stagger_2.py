# def staggered_case(string):
#     '''My initial solution used a counter to track alternating alpha chars.'''
#     result = ''
#     counter = 0
#     for char in string:
#         if char.isalpha():
#             result += char.upper() if counter % 2 == 0 else char.lower()   
#             counter += 1
#         else:    
#             result += char

#     return result

def staggered_case(string):
    '''Recreate LS solution using a boolean variable as a true/false switch'''
    result = ''
    upper = True

    for char in string:
        if char.isalpha():
            result += char.upper() if upper else char.lower()
            upper = not upper
        else:
            result += char

#     return result            


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True