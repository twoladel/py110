def bubble_sort(lst):

    swapped = True
    while swapped:
        swapped = False

        for idx in range(1, len(lst)):
            
            if lst[idx - 1] > lst[idx]:
                lst[idx], lst[idx - 1] = lst[idx - 1], lst[idx]
                swapped = True
                

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True