data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed

'''Use a for loop and an empty list to get unique list elements in order.'''

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
for num in data:
    if num not in unique_data:
        unique_data.append(num)

print(unique_data == [4, 2, 1, 3])
