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

import random

WIN_CONDITIONS = [
    {1, 2, 3},
    {1, 4, 7},
    {1, 5, 9},
    {4, 5, 6},
    {7, 8, 9},
    {2, 5, 8},
    {3, 6, 9},
    {3, 5, 7}
]

def initialize_board():
    return {num: ' ' for num in range(1, 10)}


def display_board(board):
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')


def prompt(message):
    print(f'==> {message}')


def player_choice(board):
    options = [key for key, value in board.items() if value == ' ']
    square = 0
    while square not in options:
        prompt("Choose a square from these options: ")
        prompt(f'{options}')
        square = int(input())

    return {square: 'X'}


def computer_choice(board):
    options = [key for key, value in board.items() if value == ' ']
    if options:
        square = random.choice(options)
        return {square: '0'}
    else:
        return {}


def check_for_winner(board):
    player_state = {key for key, value in board.items() if value == 'X'}
    computer_state = {key for key, value in board.items() if value == '0'}
    for condition in WIN_CONDITIONS:
        if player_state >= condition:
            return 'User wins!'
        elif computer_state >= condition:
            return 'Computer wins!'


def check_for_draw(board):
    return not [key for key, value in board.items() if value == ' ']


def play_round(board):
    board |= player_choice(board)
    board |= computer_choice(board)
    display_board(board)

def play_game():
    while True:
        board = initialize_board()
        display_board(board)

        while True:
            play_round(board)
            winner = check_for_winner(board)
            if winner:
                print(winner)
                break
            draw = check_for_draw(board)
            if draw:
                print("It's a draw")
                break
        
        prompt('Continue playing? Enter y or n')
        answer = input()
        if answer[0] in {'n', 'N'}:
            break

play_game()