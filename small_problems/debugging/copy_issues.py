import copy

original = [[1], [2], [3]]
# copied = copy.copy(original)
copied = copy.deepcopy(original) # use deepcopy to make new nested lists too.

original[0][0] = 99

print(copied[0] == [1])

