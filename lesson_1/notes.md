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
- `{key: value}`
- Ordered as of Python 3.7 
- mutable
- keys must be hashable objects
    - `TypeError` raised if unhashable object used as key
    - `int` and `str` are best options for keys
    - `frozensets` and `ranges` next
    - `tuple` if all elements hashable
    - `float` **BEWARE** risky due to floating point precision issues
- Referencing a key that doesn't exist will raise `KeyError`
    - Avoid with `dict.get()` method -- will return `None` or specified return value if key not present
- Check membership of dict keys with `in` and `not in` keywords
- `del` statement to delete key: value pairs

#### Hashing
- object is hashable if it has a stable and *mostly* unique **hash value**
- hash value is determined by the `hash` function 
- relied on for quick data retrieval (dicts, sets)
- hash collions happen if two keys have the same hash value, Python deals with it, but can cause efficiency issues

### Sets
- also use {} notation
- unordered collection on unique elements (i.e. no duplicate values)
- mutable
    - elements must be immutable (hashable) this helps keep elements unique
    - `TypeError` if you attempt to add a mutable element
- `in` keyword to check for membership
- `remove` method will raise a `KeyError` if element not in the set
- `discard` method will not raise an error if element not in the set

### Frozen Sets
- `({})`
- Same as sets but immutable (hashable)
- membership tests `in` or `not in`

### Operations on Dicts, Sets and Frozen Sets
- membership testing: `in` and `not in`
- determine length: `len`
- iteration: never with indexes, for `dict` iterates over keys
- `clear` method to remove all elements from `set` or `dict`
    - not `frozenset` because they are immutable

### Conversion to Dicts, Sets, and Frozen Sets
- Converting to Dict:
    - need pairs of data, like a list of tuples where each tuple is a pair
    - can use `zip` to create pairs and then use the `dict` function
    ```
    >>> keys = ['a', 'b', 'c']
    >>> values = [1, 2, 3]
    >>> zipped_pairs = zip(keys, values)
    >>> dict(zipped_pairs)
    {'a': 1, 'b': 2, 'c': 3}
    ```
- Converting to Sets and Frozen Sets
    - use the `set()` and `frozenset()` constructors
    - converting to one of these will ensure only unique elements 
    - can convert sets and frozensets to each other

## 5. Working with Strings and Ranges
