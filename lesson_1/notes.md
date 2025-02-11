# Lesson 1 Assignments

## 2. Intro to collections in Python
### sequences
Sequences are ordered collections. In a sequence each element has a definite position,
defined by its index, that starts at 0 and increments by one for each subsequent
element. 
- `str` (sometimes called text sequences)
- `list`
- `tuple`
- `range`

### other collections
Unordered collectins that are often used in python:
- `dict`
- `set`
- `frozenset`

## 3. Sequences
### Lists
- `[]`
- reference elements with indexing `lst[0]`
- must use index notation for element reassignment
- `IndexError` raised when trying to access index that is out of range
- mutability (lists are the only mutable sequence)

### Tuples
- `()`
- ordered collections, but immutable. 
- access elements with indexing `fruits[0]`
- Immutability:
```
>>> fruits = ("apple", "banana", "cherry")
>>> fruits[0] = "strawberry"
TypeError: 'tuple' object does not support item assignment
```
- Want to change the contents of a tuple, reassign to a new tuple

### Strings
- `""`
- indexing and IndexError the same as lists and tuples
- store a represent text based information
- collection of chars (a lone char is a `str` of length 1)
- immutable

### Ranges
- use range constructor: `range(5)` `range(1, 10, 2)` etc.
- `range(start, stop, step)` (stop is not included in the range)
- memory efficient because only stores start, stop, step and current value.
- next element computed based on current state of range, but only when needed
- indexing and IndexError are the same 
- immutable
- use `list()` or `tuple()` constructor to expand range

### Operations on Sequences
#### Slicing
- syntax: `sequence[start:stop:step]`
- stop not included in the subset, same as a range
- `start` defaults to 0 (or -1 for negative steps)
- `stop` defaults to last element (or 0 for negative steps)
    - if a stop is not given.
    - stop is not included, if given
- `step` defaults to 1 (negative steps descend from end of list to beginning)
- if start > stop, you'll get an empty collection and vice versa if it is a negative step.
- `my_list[::]` or `my_list[:]` create a shallow copy (pythonic)
    - shallow copies are a new object
    - but if they contain nested collections, those nested objects are same object

#### Determine length
- `len()`

#### Iterating over sequences
- `for loop` most common and idiomatic 
- later assingment will show `for loop` with `enumerate()` to get indexes while iterating

#### Concatenating with + operator
- returns a new object by appending sequence on right of `+` to sequence on left.
    - never mutates original sequence, always creates new sequence
- can't concatenate `range`

#### Using `count` and `index` methods
- Can use either method on all sequences
- `sequence.count(value)` - returns number of occurences
- `sequence.index(value)` - returns index of first occurence
    - `index()` raises a `ValueError` if value not present

#### Finding Minimum and Maximum
- `min()` and `max()` are available for all sequences
- numerical values = common sense
- strings are compared lexographically by Unicode value
- if lists or tuples contain mixed data types, `min` and `max` are unlikely to work

### Conversion to Lists, Tuples and Strings
- Use the `list()` and `tuple()` constructors
- They will preserve the order of the sequence you're converting
- Converting to a string can be done w/ `str()` constructor... **BUT**
    - `join()` method is preferred, although all elements must be `str` objects
- Want to `join` a collection that has non-string elements? 
    - Use a list comprehension w/ `str()`! 

```
>>> my_list = [1, 2, 3, 4]
>>> ', '.join([str(element) for element in my_list])
'1, 2, 3, 4'
```

- Ranges: construct ranges you need 
    - don't bother trying to convert another collection to a range

## 4. Dictionaries, Sets and Frozen Sets

### Dictionaries