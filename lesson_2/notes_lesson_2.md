# Lesson 2 Assignments

- [Sorting](#2-sorting)

## 2. Sorting

### Sorting in Python basics
- Sorting is an operation that puts a collection in order based on a specific criteria
- Difference between `sorted()` and `list.sort()`
    - `sorted()` returns a new list and leaves the old list alone (non-destructive)
    - `.sort()` method sorts the list in place, mutating the orignal list object
- Can't sort a string in place as it is immutable, but you can call `sorted()` and then use `join`

### Sorting lists of strings
- alphabetic first
- Unicode standard code point second (a lowercased word will come after an uppercase word)
    - `ord()` returns the code point of a character. 

### Unicode code point rules to remember (recall the bullets)
- Digits and some punctuation come before letters
- Uppercase letters come before lower case letters
- Several punctuation chars betweeen uppercase and lowercase letters
- After lowercase letters more punctation and other special characters
- There are various 8-bit encodings that include additional characters beyond the 7-bit ASCII
    - This is extended ASCII
    - These are code points 128-255
- Starting at code point 256 is the remainder of the unicode characters
    - various scripts and symbols

### Reverse sorting
- `sorted('string', reverse=True)`
- `my_list.sort(reverse=True)`

### Custom Sorting

#### First class and Higher Order Functions
- first class objects are objects that can be assigned to a variable or used as an element in a collection
- all data types including custom data types in Python are first class objects
- in Python functions are also first class objects
    - called: first class functions
- Some functions can take functions as arguments and return functions: ***Higher Order functions*** 
    - `sorted` and `list.sort` can take functions as `key` in keyword arguments
    - They are high order functions
- Built-in functions like `len` and `str.lower` are examples of first class functions that can be passed as keys
- Sometimes you need more customization in your sorting 
    - **(EXAMPLE below in summary)**
    - write functions to use as sorting keys
    - write functions that return a tuple and `sorted`, `list.sort` will sort based on the tuple
    - tuple sorted by first value and then second if first value is equal, etc. 
    - tuple can be more than two elements

### Summary
- `sorted` and `list.sort`
- `reverse=True` for reversing the sort
- using built in and custom functions as keys to sort by:
    - sorted(my_list, key=str.lower)
- *complex sorts* require defining your key in a function that returns a tuple
    - make the order of the tuple, the order you want the criteria to sort by
    - example below, we sort by length of word and then alphabetically
    ```
    lst1 = [
    'apple',
    'bear',
    'Johnny!',
    'Once Upon a...',
    'jeurske',
    'cat',
    'zebra',
    'ant',
    'zoo',
    'blueberry tea'
    ]

    def list_key(element):
        word = element.lower()
        length = len(element)
        return (length, word)

    print(sorted(lst1, key=list_key))
    # output: ['ant', 'cat', 'zoo', 'bear', 'apple', 'zebra', 'jeurske', 'Johnny!', 'blueberry tea', 'Once Upon a...']
    ```

## 3. Sorting Practice Problems
1. easy
2. easy
3. easy
4. pretty easy. solution below:
    ```
    def book_year(book):
    return int(book['published'])

    books.sort(key=book_year)
    ```

## 4. Nested Data Structures
### Referencing collection elements
- index chaining to *reference* inner list elements of a nested list
```
lst = [[1, 3], [2]]
print(lst[0[1]]) # 3
``` 

### Updating Collection elements
- use index chaining again to reassign elements of an inner list
    - `lst[0][1] = 5`
- the first half of the chain is the element reference
    - `lst[0]`
- the second half of the chain is the element reassignment
    - `[1] = 5`
- if you want to insert into a nested list, chain with `append()`
    - `lst[0].append(7)`
    - `lst[1].append([9])`  # this one nests another list into the nested list

### Other Nested Structures
- lists and tuples can contain all sorts of data types
- example:
```
lst = [3, {"b": "bear"}, (1, [2, 3, 4], 5), {6, 7}]

print(lst[0])        # 3
print(lst[1])        # {"b": "bear"}
print(lst[1]['b'])   # 'bear'
print(lst[2][1])     # [2, 3, 4]
print(lst[2][1:])    # ([2, 3, 4], 5)
print(lst[2][1][2])  # 4
print(lst[3])        # {6, 7}
```

- sets and frozensets can also have various data types but all must be hashable! 
    - can't have lists, dicts, or sets as elements in a set or frozenset
- the above is true for dict keys 
    - whereas dict values can be hold anything like lists and tuples can.

### Variable References for Nested collections
- when you add variable references to collections to a collection, you're addding references to those nested collections to the outer collection. 
- Here is how I explained it to LSBot, which LSBot confirmed was correct.
- @LSBot
 I'm working through assignment 4 in lesson 2: Nested Data Structures. The section Variable References for Nested collections has this example.
```
a = [1, 3]
b = [2]
lst = [a, b]
print(lst)          # [[1, 3], [2]]
```
- It is explained that the variable `lst` is assigned to a list object containing references to the list objects referenced by `a` and `b` . My question is specfically about the variables as pointer diagram. Is it technically true that the variable `a` is pointing to the address in memory of the list object it references and thus the same with variable `b` , meaning that the variable `lst`  points to the address of its list object but contained at that location in memory are the addresses of the two nested list objects referenced by variables `a` and `b`?

- So you could update the list referenced by variable `a` in two ways now:
    - `a[0] = 2` **OR** `lst[0][0] = 2`

### Shallow Copying
