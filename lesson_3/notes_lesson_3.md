# Lesson 3 assignments

## 2. Debugging with pdb
### Basics from PY101 assignment:
- `import pdb` in the file you want to debug
- `pdb.set_trace()` set breakpoints with this function call
- use `c` to continue after breakpoint
- use `n` to see the next line of code
- use `p` to print 
    - `p variable_name` will print the current value of said variable
    - `p expression` will print return value of the expression
    - `p` combinined with a new expression not in the current code to test solutions.
        - if a current expression isn't providing the expected result, use `p` to try alternate solutions. 
- use `q` to quit the debugger

### Executing expressions
- you can execute expressions in the debugger to test code
    ex *see the print calls below*:
    ```
    > /Users/xyzzy/ls_test/test.py(10)
    -> counter += 1
    (Pdb) print(counter)
    1
    (Pdb) print(counter + 5)
    6
    ```
### Setting and Clearing Breakpoints
- other than using the `set_trace` function
- dynamically set breakpoints within the debugger with `b line #`
    - ex: `b 6` would set a breakpoint at line 6 of the program
- breakpoints have numbers as you set them: 1, 2, etc.
- use `cl breakpoint #` to clear a breakpoint: `cl 1` for example

### Stepping thru and into Functions
- `n` for next will move to next line of code, if next line is a function it will let the function run
- `s` for step will let you step into the function and examine it line by line
    - within the function, use `s` to continue to step through it. 
- `r` to finish running the function

### Other useful pdb commands
- `help` displays overview of available commands
- `list` will display 11 lines of code, the line you're on, plus 5 before and after
    - can specify which lines `list 10,20` would give lines 10 thru 20 inclusive
- `where` displays a stack trace to your current position.
    - ends with last function call
    - starts with where execution started

## 3. Tic Tac Toe problem decomposition
- Build a tic tac toe program that lets a user play the computer

### Describe tic tac toe
- 2 player game
- played on a 3 x 3 grid
- alternating placing X's and 0's 
    - one player is X's
    - one player is 0's
- three in a row wins (in any direction)
- if all 9 squares are filled and no one has 3 in a row it is a tie.

### Steps of the program
- Display the empty game board
- Prompt 1st player to mark a square
- Computer marks a square
- Display the updated game board
- continue alternating between players until (implies we'll need checks each time)
    - a player has three in a row
    - all nine squares are marked
- Announce winner or tie

### Flowchart
- wrote out a flowchart in blue notebook with PY100/PY101 notes in it. 
- flowchart shapes are inaccurate in that diagram