# Lesson 1 Assignments

- [Intro to collections in Python](#2-intro-to-collections-in-python)
- [Sequences](#3-sequences)
- [Dicts Sets and Frozen Sets](#4-dicts-sets-and-frozen-sets)
- [Working with Strings and Ranges](#5-working-with-strings-and-ranges)
- [Working with Lists and Tuples](#6-working-with-lists-and-tuples)
- [Working with Dicts, Sets, and Frozen Sets](#7-working-with-dicts-sets-and-frozen-sets)
- [Unpacking Iterables in Python](#8-unpacking-iterables-in-python)
- [Intro to the PEDAC process](#9-intro-to-the-pedac-process)
- [PEDAC problem solving process](#10-the-pedac-problem-solving-process)
- [PEDAC Guided Practice: Leftover Blocks](#11-pedac-guided-practice-leftover-blocks)
- [PEDAC Guided Practice: Most Adjacent Consonants](#12-pedac-practice-sort-by-most-adjacent-consonants)
- [Selection and Transformation](#13-selection-and-transformation)

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

## 4. Dicts Sets and Frozen Sets

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
    - can also use `enumerate` with `dict` to create a dict 
    ```
    >>> lst = ['a', 'b', 'c', 'd']
    >>> my_dict = dict(enumerate(lst))
    >>> print(my_dict)
    {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
    ```

- Converting to Sets and Frozen Sets
    - use the `set()` and `frozenset()` constructors
    - converting to one of these will ensure only unique elements 
    - can convert sets and frozensets to each other

## 5. Working with Strings and Ranges
### Working with Ranges
#### old range info
- how to construct with start, stop, step
- iteration is popular usage
#### New Range info
- `enumerate` function when you need index and element during iteration
```
colors = ['red', 'green', 'blue']
for idx, color in enumerate(colors):
    print(f'{color} is at position {idx}')

red is at position 0
green is at position 1
blue is at position 2
```
- range attributes:
    - `.start`, `.stop`, `.step`
    - if you have a range object and don't know how it was constructed you can use the attributes to get info
    ```
    start = range.start # No () when using range attributes
    ```

### Working with Strings

#### `str.count` `str.index` `str.find`
- pass substring as argument
- `index` returns an error if value not found `ValueError`
- `find` returns `-1` if value not found
- all three take optional start and stop args (stop works like in ranges or slices)

#### `str.replace`
- args: (old, new, count)
- replaces old arg with new arg (args must be substrings)
- count arg is optional - if you leave blank will replace all instances
- returns copy of string with new in place of old

#### `str.upper` `str.lower` `str.casefold`
- all three methods change case on entire string
- `casefold` is internationlized (best practice)

#### `str.capitalize` and `str.swapcase`
- `capitalize` will upper the first character and lower the rest of the string
- `swapcase` will swap the case of all cased characters in the string
- `swapcase` is internationalized - potential unexpected behavior if doubling calls (see below)
```
>>> 'Straße'.swapcase()
'sTRASSE'

>>> 'Straße'.swapcase().swapcase()
'Strasse'
```

#### `str.join` and `str.split`
- `join` takes an iterable (all elements must be strings) and returns them as a string
    - precede `.join` with a whitespace char `" "` or other chars to place between elements
- `split` splits a string into a list of substrings
    - takes two optional args
    - no args will split at any sequences of whitespace
    - delimiter arg to split at all occurences of delimiter
    - second arg is amont of splits, if you don't want all splits
    - string.split('') - can't split on empty string, just call `list` or `tuple`

#### `str.strip` `lstrip` and `rstrip`
- will remove whitespace from both sides or left only or right only
- optionally pass it an argument string
    - it will remove all occurences of any chars in that string until it meets a char not in string

#### other methods
- `startswith` and `endswtih`
- `isalpha` `isalnum` `isspace` `isdigit`
    - above, all chars must be to return `True`

## 6. Working with Lists and Tuples

### Working w/ Lists

#### `list.count`
#### `list.index`
- optional stop and end arguments for `index`
#### `list.append`
#### `list.insert`
- two arguments:
    - first arg is index where the object will be inserted 
    - the second argument is the object you're inserting into the list
    - if first arg is > len(list), will simply append
#### `list.extend`
- extend a list with another iterable
- appends list with entire iterable 
- if adding from a set or frozenset, items might not be appended in expected order because sets are unordered

#### `list.remove` and `list.pop`
- `pop` mutates list and returns 'popped' element
    - takes an index as arg (if no arg, removes and returns last element)
    - `IndexError` if passed an out of range index argument
- `remove` mutates list and returns `None`
    - takes an object as an argument
    - `ValueError` if object not present

#### `list.reverse`
- returns `None` and reverses the list in place

#### `list.sort`
- returns `None` and sorts the list in place
- key argument creates opitons 
- pass `sort` any function or method that takes one argument and returns a value
- if sorting incompatible types, will raise `TypeError`
- reverse the sort with `reverse=True` keyword argument
- can use a `key` function to ensure all elements are of same type
    - ex. ensuring any `ints` are converted to `str` or that all collections are `list`

### Working w/ Tuples

#### Tuple Unpacking
```
>>> shades = ('crimson', 'emerald', 'azure')
>>> r, g, b = shades
>>> r
'crimson'

>>> g
'emerald'

>>> b
'azure'
```
- above example shows that tuples can be unpacked into variables
- also used with enumerate function and for loops
- remember tuple of one needs a trailing comma `('tuple',)`
- `index` and `count` are most common methods for tuples

### Converting Dicts to lists and tuples
- wrap the dict method calls in `list()` or `tuple()`
- example below:
```
>>> data = {'apple': 5, 'banana': 3, 'cherry': 8}
>>> list(data.values())
[5, 3, 8]

>>> tuple(data.values())
(5, 3, 8)
```

### Converting Sets and Frozen Sets to lists and tuples
- if you need your set (or frozenset) to be ordered
- covert to a list or tuple depending on if you want immutability or not
- may need to sort after converting (does the order matter to you?)

## 7. Working with Dicts, Sets and Frozen Sets
### Dicts
- access values via keys
- delete key-value pair with `del` statement
- check for keys with `in` or `not in` before accessing to avoid errors
- use `copy` method if you want a new copy of dict and not a new reference
    - remember shallow copy so nested mutable objects are same and will update if mutated
#### `get` and `setdefault` method
- `get` will take a second argument which is a default value to return if key doesn't exist
- `setdefault` takes a key and default value as arguments
    - if key is **NOT** present, `setdefault` will add key and default value to the dict 
        - *AND* return the value
    - if key is present, `setdefault` will return the value
    - `setdefault` is helpful for initializing dicts. example below
    ```
    word = "hello"
    letter_counts = {}
    for letter in word:
        letter_counts.setdefault(letter, 0)
        letter_counts[letter] += 1

    print(letter_counts)
    ```
#### `pop` and `popitem`
- `pop` will remove the key-value pair and return the value
    - `pop` *requires* a key as the argument
    - if the key doesn't exist, `KeyError`
    - to avoid error, add a default value as the second arg to be returned if no key
- `popitem` will remove the key-value pair and returns the pair as a **tuple**
    - `popitem` takes *no arguments* and removes last key-value pair 
    - will return `KeyError` if dict is empty

#### Merging Dictionaries: `update`, `|`, `|=`
- `update` method will add the argument dict to the dict you call the method on.
    - if keys overlap, value from arg dict will overwrite
    - `dict.update(new_dict)`
- `|` is the merge operator
    - will not mutate either dict, will merge like `update` but create a *new dict object*
    - `merged_dict = dict | new_dict`
- `|=` is the update operator
    - will do exactly what update method does
    - `dict |= new_dict`

#### Converting to Dicts
- ***Requires iterable being converted to have key-value pairs***

### Sets
- Check if values exist with `in` and `not in`
#### Checking for subsets and supersets
- `issubset`, `<=`, `<`
- `issuperset`, `>=`, `>`
- the methods and operators containing `=` will return `True` if equal
- `<` and `>` only return `True` if left side is sub or super of right but **NOT EQUAL**

#### Set operations
- `union` method and `|` operator
    - will return a new set by combining two sets - **No mutation**
    - `set1 |= set2` reassignment syntax will mutate `set1`. `|=` is the `update` operator
- `intersection` method and `&` operator
    - checks for common elements between sets and returns them as a new set object
    - No mutation
- `difference` method and `-` operator
    - checks for differences between the sets
    - returns values (as a new set) from left side operand (or calling set) that are not in right side operand
    - No mutation

#### Checking disjoint sets `isdisjoint`
- disjoint means that there are no overlapping elements between sets
- returns a boolean

#### Copying a set `copy`
- copy method can be used to create a new set object with same elements
- `=` assignment will create a new reference to same set object

#### Adding and remvoing set members: `add`, `remove`, `discard`, `pop` and `clear`
- `add` method: adds passed argument to set and returns `None`
    - No error if element is already a member
- `remove` method: removes passed argument from set and returns `None`
    - `KeyError` if element is not a member
- `discard`: same as remove but won't raise an exception if argument is not a member
- `pop` removes a random element from the set and returns it
    - `pop` takes no arguments
    - Use if you want to empty a set one element at a time 
    ```
    fruits1 = {"apple", "banana", "cherry"}

    while fruits1:
    print(fruits1.pop())
    ```
    - will raise a `KeyError` if you call `pop` on an empty set
- `clear` removes all elements from the set and returns `None`

#### Set methods vs operators
***For all methods that have an operator counterpart***
- you can pass any iterable to the methods
    - Non-mutating: `union`, `intersection`, `difference`, `symmetric_difference`, `issubset` and `issuperset`
    - Mutating: `update`, `intersection_update`, `difference_update`, `symmetric_difference_update`
- operators need both operands to be `set` or `frozenset`
- whether using method or operator, you can have several arguments or operands
    `set1.union(set2, set3)` or `set1 | set2 | set3`
#### Converting to a set
- convert other collections to sets with `set()` 
    - remember that it won't maintain order

### Working with Frozen Sets
- can use set methods like `union` to create new frozensets
- can't use mutating methods like `pop`
- Useful if we want 'sets' as dictionary keys since sets themsevles aren't hashable

## 8. Unpacking Iterables in Python
### The Unary Operator `*`
- the `*` operator is used to unpack iterables
- it should be placed before the iterable to unpack: `*lst`
- if you want to combine iterables of different types:
    - `merged_list = [*lst, *tup1, *set, *tup2]` 
    - the above syntax would create a new list combining all elements from those iterables
    - you can also merge as a tuple or a set
- if you want to pass the elements of an iterable as separate args
    ```
    def test(num1, num2, num3):
    # do something

    numbers = [1, 2, 3]
    test(*numbers)
    ```
    - amount of elements in iterable must match amount of args in definition

### Unpack an iterable into variables - variable assignment
```
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # Outputs: 1 2 3
```
- this does not require the Unary operator `*`
- amount of elements in the iterable must match amount of variables being assigned
    - will raise `ValueError` if they don't match
- supports nested unpacking too
```
numbers = [1, [2, 3, 4], 5]
a, (b, c, d), e = numbers
print(a, b, c, d, e)  # Outputs: 1 2 3 4 5
```

### The Unary `**` Operator for Dictionaries 
- can be used to unpack dicts
- example: to merge to dicts together
```
>>> dict1 = {'a': 1, 'b': 2}
>>> dict2 = {'b': 3, 'd': 4}
>>> merged_dict = {**dict1, **dict2}
>>> merged_dict
{'a': 1, 'b': 3, 'd': 4}
```

- Also `**` can be used to collect or pack items into a dict
- example below with keyword arguments (`kwargs`) into a function:
```
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(name="Srdjan",
        age=38,
        profession="software engineer")

# Output:
# name: Srdjan
# age: 38
# profession: software engineer
```

## 9. Intro to the PEDAC process
- P - Understand the ***P***roblem
- E - ***E***xamples and Test cases
- D - ***D***ata Structure
- A - ***A***lgorithm
- C - ***C***ode

### - P: Understand the Problem
1. Read the problem description
    - determine inputs and outputs
        - **Outputs**: always verify if you are returning the *same object* or a *new object*
    - note any explicit requirements
2. Check the test cases
    - these give info about implicit requirements not mentioned in the problem description
    - some implicit requirements may not be answered by the test cases, so ***ASK***
3. If any part of the problem is unclear, ask the interviewer for clarification


4. To conclude this step (P), write down: 
    - input
    - output (same object or new object?)
    - rules
        - explicit requirements
        - implicit requirements

### - E: Examples and Test Cases
- not covered here because interviewer will provide. Covered in a later course

### - D & A: Data Structure and Algorithm
- after working through Understanding the Problem, determine the data structure needed
- then build the algorithm
- See pedac_palindrome.py file for first practice at creating algorithm
    - write high level abstraction
        - example could be naming functions that you'll later need to make an algorithm for
    - then write informal pseudocode for the "hard" parts
    - finally write code from pseudocode
    - breakdown each piece into smaller chunks to solve then move on

## 10. The PEDAC problem solving process 
- Notes on the videos below
- Following along with solving problem in video with PEDAC in .py file
    - sum_even_num_rows.py

### Video 1: P - Understanding the Problem
- Establish the rules and boundaries of the problem
- Restate the problem in our own words
- Note rules:
    - Explicit requirements
    - Implicit requirements
- Determine the input and output
- Ask questions / indentify unclear info
- Don't Rush!! Spend time here ensuring you **UNDERSTAND**

### Video 2: E - Examples and Test Cases
- Can be used to confirm or refute assumptions about the problem
- Answer questions and clarify implicit requirements
- Test cases are written in code to be run to test your solution
- Codify rules and boundaries of the problem

### Video 3: D - Data structure
- Thinking in terms of data structures is important part of problem solving
- Data structures help us think logically about the solution
    - reason with data logically
    - helps interact with data at the implementation stage
- Data structures are closely linked to the algorithm in the next step

### Video 4: A - Algorithm
- A logical sequence of steps to solve a problem (complete a task)
- Closely related to data structure
- At first keep it high level abstraction, avoid thinking about code implementation
- Then you can begin to get granular on each step
- Break down steps and add detail as needed
- Don't worry about efficiency at this stage
- Use PEDAC for a step in your high level algorithm if complex

### Videos Implementing code parts 1-6
- Translate your algorithm into working code
    - Think about algorithm in context of the programming language
        - Features and boundaries
        - Rules of data structures
        - Built-in methods and functions
        - Syntax / general patterns
    - Create test cases if not provided
- Code with intent

### Final thoughts on PEDAC
- Not a linear process
- Move back and forth between the steps
- Refer back to notes 
- Switch between implementation and abstract problem solving
- Don't try to problem solve at the code level
- Practice, practice, evolve, practice, evolve.

## 11. PEDAC Guided practice: Leftover Blocks
Notes here for this assignment and the steps of PEDAC
leftover_blocks.py for my code implementation

### 1. Understand the Problem:
- Tasks
    - Mental model of the problem
    - Input(s)
    - Output(s)
    - Explict and implicit requirements
    - Clarifying questions 

- Restate: After given a number of blocks. Determine the tallest building we can make with those blocks. Calculate the number of leftover blocks.
- Input: integer that represents the number of blocks we have to build with
- Output: new integer representing the number of blocks we have leftover
- Explicit requirements:
    - each block is a cube: six equal sided box
    - the structure we are building is in layers
    - the top layer is a single block
    - a block in an upper layer must be supported by four blocks in lower layer
    - a block in a lower layer can support more than one block above
    - No gaps between blocks
- Implicit requirements:
    - a valid structure is a minimum of 1 layer
    - input of 0 should return 0
    - each layer's block count is the square of the layer number (top to bottom):
        - e.g. layer 2 would have four blocks because 2 squared is 4 and then layer 1 would be 1
    - build one layer at a time, incrementing and squaring
- Questions: (updated requirements above after answering questions from test cases)
    - Can we have a structure of a single layer? - Yes
    - What should the output be if we get a 0 input? - 0
    - LS: Can a lower layer be valid if it has more blocks than it needs? - No

### 2. Examples and Test Cases
- The provided examples (copied into the leftoverblocks.py file) answered my questions from step 1

### 3. Data Structure
- working with squares and square roots
- ints and mathematical operators
- perhaps a dict or nested list to represent layers and total block count for that amount of layers?

### 4. Algorithm
- note from first step: build one layer at a time, incrementing and squaring
- Given total block count
- 1. Build a layer
    - start at layer 1 // *update*: start at layer 0
    - ***Did not have this step initially***: set remaining blocks to input
    - ***Nor this step***: increment layer by 1
    - ***Needed to move this step into step 3*** subtract that amount of blocks from total block count
        - ***and this step*** updating total block count  
- 2. Calculate size of next valid layer: increment layer by 1 and square the layer number
- 3. Check if enough blocks for next layer: is total block count >= amount needed for next layer
    - if yes, repeat steps 1 & 2
    - else: return remaining blocks

- My step 1 kept tripping me up. Made notes above of how I adjusted based on LS's solution.
- When I tried to implement off of LS's algorithm, it when smoothly

## 12. PEDAC practice Sort by Most Adjacent Consonants
- did this problem before. 
- removed PEDAC notes

## 13. Selection and Transformation
- Selection: choosing items from an iterable depending on one or more criteria
- Transformation: modifying each element of a collection based on criteria
- both use basics of looping:
    - a loop
    - a counter
    - a way to retrieve the current value
    - a way to exit the loop

### Using loops to select and transform
- selection criteria will be in form of conditional
     - ex. `if num % 2 == 1` is a selection criterion
     - this example selects odd numbers
- transformation criteria will be a line performing an operation
    - ex. `num * multiplier` is a transformation criterion
        - mulitplying the number by the multiplier to change it

- When performing a transformation, it's always important to pay attention to whether the original collection is mutated or if a new collection is returned.

### Extracting to Functions
- when doing selections or transformations on collections, extracting to a function is good practice
- if your combining selection and transformation: 
    - and none of the elements of a collection fit the criteria for selection
    - a transformation still happended even though elements did not transform
    - This is an identity transformation

### More flexible functions
- as we're writing functions to select or transform collection elements
    - we can make the functions more generic to be more flexible
    - example:
    ```
    def multiply(numbers, multiplier):
    multiplied_nums = []

    for current_num in numbers:
        multiplied_nums.append(current_num * multiplier)

    return multiplied_nums

    my_numbers = [1, 4, 3, 7, 2, 6]
    print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]
    ```
    - in the above example, we can now use this function to multiply any list of numbers by any number
### Summary
- always be thinking about return values
- are we returning new collection objects or mutating?
- additional function parameters add flexibility to select and transform functions