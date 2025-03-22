# def is_balanced(phrase):
#     open_paren = 0
#     close_paren = 0

#     for char in phrase:
#         if char == '(':
#             open_paren += 1
#         if char == ')':
#             close_paren += 1
#         if close_paren > open_paren:
#             return False
    
#     if open_paren == close_paren:
#         return True
    
#     return False

# print(is_balanced("What (is) this?") == True)        # True
# print(is_balanced("What is) this?") == False)        # True
# print(is_balanced("What (is this?") == False)        # True
# print(is_balanced("((What) (is this))?") == True)    # True
# print(is_balanced("((What)) (is this))?") == False)  # True
# print(is_balanced("Hey!") == True)                   # True
# print(is_balanced(")Hey!(") == False)                # True
# print(is_balanced("What ((is))) up(") == False)      # True


OPENS = {'(', '"', "'", '{', '['}
CLOSE = {')', '"', "'", '}', ']'}
PAIRS = {'()': 0, '""': 0, "''": 0, '{}': 0, '[]': 0}

def is_balanced(phrase):
    for char in phrase:
        for elem in PAIRS.keys():
            if char in elem:
                if char in OPENS:
                    PAIRS[elem] += 1
                if char in CLOSE:
                    PAIRS[elem] -= 1
                if PAIRS[elem] < 0:
                    return False
    if any(PAIRS.values()):
        return False
    return True

print(is_balanced("{}") == True)
print(is_balanced("[]") == True)
print(is_balanced("()") == True)
print(is_balanced("{[({})]}") == True)
print(is_balanced("\"{[('')]}\"") == True) 
print(is_balanced("Hello [Python] (asdf).") == True)
print(is_balanced("{[()stacks]} are {kool[()]}") == True)
print(is_balanced("{[}]") == True)
print(is_balanced("({[})") == False)
print(is_balanced("][") == False)
print(is_balanced("'''") == False)
print(is_balanced("'\"'\"'") == False)

