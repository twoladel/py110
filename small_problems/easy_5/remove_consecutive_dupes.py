def unique_sequence(numbers):
    if not numbers:
        return []
    
    result = [numbers[0]]
    for idx, num in enumerate(numbers[1:], start=1):
        if num != numbers[idx - 1]:
            result.append(num)

    return result


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

print(unique_sequence([]) == []) # True

original = [1, 1, 2, 2, 2, 1, 1, 3, 2, 2, 9, 1]
expected = [1, 2, 1, 3, 2, 9, 1]
print(unique_sequence(original) == expected) # True