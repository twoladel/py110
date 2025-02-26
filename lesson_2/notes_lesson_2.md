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
    - write functions to use as sorting keys
    - write functions that return a tuple and `sorted`, `list.sort` will sort based on the tuple
    - tuple sorted by first value and then second if first value is equal, etc. 
    - tuple can be more than two elements

### Summary
- `sorted` and `list.sort`
- `reverse=True` for reversing the sort
- using built in and custom functions as keys to sort by:
    - sorted(my_list, key=str.lower)

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
