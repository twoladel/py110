'''
Can't mutate a set while iterating because sets are not sequences. 
Made the data set a list for iteration to fix.
'''
data_set = {1, 2, 3, 4, 5}

for item in list(data_set):
    if item % 2 == 0:
        data_set.remove(item)

print(data_set)

# Pythonic solution is to use a set comprehension
data_set = {1, 2, 3, 4, 5}

data_set = {item for item in data_set if item % 2 != 0}
print(data_set)

