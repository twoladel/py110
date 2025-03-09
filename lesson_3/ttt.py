'''Write a tic tac toe program for a user to play the computer.'''

'''
Basic steps for the program:
1. Display the empty board
2. Prompt user to pick a sqaure
    - easy use input() 
    - what kind of input do I want? 
        row # and col # (thinking nested lists)
3. Computer picks a square
    - use random module for computer selection
    - start with a list of possible choices (tuples)
        - choices are tuples: (row #, col #)
    - randomly select a tuple from the list. 
    - when either player picks a square, remove it from the set
4. is there a winner? 
    if yes, display the winner
        and ask to play again.
    if no, is the board full?
        if yes, display DRAW
            and ask to play again.
        if no, display the current board and prompt user
'''
'''
PEDAC for updating the board
When we mark a 'square' on the board, we want to place an X or 0 in the middle.
Second print statement of the row and the third space within specified column.
Use f-string to place variable placeholders in the middle of rows
Variables are set to empty strings (dict- keys are squares, values empty)
Pass dict with the key (square to update) and X or 0 as value 
Update game board dict and print updated board
Define game board with a dict argument
Pass empty dict to reset board
'''

def display_board(choice_dict):
    board_dict = {
        1: ' ',
        2: ' ',
        3: ' ',
        4: ' ',
        5: ' ',
        6: ' ',
        7: ' ',
        8: ' ',
        9: ' '
    }

    board_dict |= choice_dict

    print('')
    print('     |     |')
    print(f'  {board_dict[1]}  |  {board_dict[2]}  |  {board_dict[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board_dict[4]}  |  {board_dict[5]}  |  {board_dict[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board_dict[7]}  |  {board_dict[8]}  |  {board_dict[9]}')
    print('     |     |')
    print('')

choice_dict = {}
display_board(choice_dict)