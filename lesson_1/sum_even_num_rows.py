'''Imagine a sequence of consecutive even integers beginning with 2. The 
integers are grouped in rows. Each row contains an amount of integers
equivalent to the row number, i.e. the first row has one int, the second row
has two ints, etc. Given an integer of a particular row, return an integer
that is the sum of the integers in that row.'''

# P understand the problem
    # input: int representing a particular row
    # output: new int representing the sum of all ints in that row
    # explicit:
        # Sequence of integers 
        # Sequence begins at 2
        # Sequence is consecutive
        # Sequence contains only even numbers
        # grouped into rows
        # rows get incrementally larger
    # implicit:
        # each row contains amount of ints equal to row num 
        # only need rows up to given integer
    # questions:
        # Always a positive int being given?
        # if given number is 3: is row one contain the int, 2 and row 2 contain 4 and 6, etc?

    # visulaize the sequence:
        # row 1: 2
        # row 2: 4, 6
        # row 3: 8, 10, 12
        # row 4: 14, 16, 18, 20
        # how will we build this structure? range? nested loops?

# E - examples and test cases
    # given examples
        # Row 1 sums to 2
        # Row 2 sums to 10
        # Row 4 sums to 68
    # this mathces the visulaized sequence laid out above
    # we'll make test cases from these examples 
        # e.g. print(sum_row(2) == 10) # True

# D - data structure
    # Sequence of rows
    # order of rows is important
    # rows contain ints
    # order of ints in row is important

        # our visualized sequence is a list of nested lists
        # each nested list is a row

# A - Algorithm
    # 1. Create an empty list called 'rows' to hold our rows
    # 2. Create the first row_list and add it to 'rows'
        # PEDAC of this step below
    # 3. Repeat previous step until we have all needed rows
        # Stop when len(outer list) is equal to input value
    # 4. sum last row
    # 5. return sum

# Problem: Create a row (step 2 above)
    # Rules: 
        # Rows are a list
        # Rows contain ints
        # ints are consecutive even numbers
        # ints in each row form part of larger overall sequence
        # rows start at len 1 with int 2
        # increment size of row by 1 - rows of different lengths
        # only even numbers in row
        # once number used, can't show up again
        # start new row where old row left off

    # Input: 
        # int representing row and len of row
        # int beginning the row
    # Output: list representing the row itself

    # Examples:
        # start 2, len 1 --> [2]
        # start 4, len 2 --> [4, 6]
        # start 8, len 3 --> [8, 10, 12]

    # Data Structure:
        # List

    # Algorithm:
        # 1. Create an empty row to hold ints
        # 2. Add starting int to row
        # 3. Increment starting int by 2 and add to the row
        # 4. Repeat 2 & 3 until reached len of row (second input)
        # 5. Return the row


def sum_rows(number):
    rows = []
    starting_int = 2
    row_len = 1

    while len(rows) < number:
        inner_row = build_row(starting_int, row_len)
        rows.append(inner_row)

        starting_int = (2 + inner_row[-1])
        row_len += 1

    return sum(rows.pop())


def build_row(start_num, length):
    row = []
    while len(row) < length:
        row.append(start_num)
        start_num += 2
    
    return row

# Test cases:
print(sum_rows(2) == 10) # True
print(sum_rows(4) == 68) # True
print(sum_rows(3) == 30)