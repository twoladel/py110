import os
import random

EMPTY_SQUARE = ' '
PLAYER_MARK = 'X'
COMPUTER_MARK = '0'
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
    os.system('clear')

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


def empty_squares(board):
    return [key for key, value in board.items() if value == EMPTY_SQUARE]


def join_or(lst, delimiter=', ', joining_word='or'):
    if len(lst) == 2:
        return f'{lst[0]} {joining_word} {lst[1]}'
    elif len(lst) > 2:
        last_num = lst.pop()
        choices = delimiter.join(lst)
        return f'{choices}{delimiter}{joining_word} {last_num}'
    
    choices = delimiter.join(lst)
    return f'{choices}'


def player_choice(board):
    options = empty_squares(board)

    while True:
        valid_choices = [str(num) for num in options]
        prompt("Choose a square from these options: ")
        prompt(join_or(valid_choices))
        square = input()
        if square in valid_choices:
            break

    board[int(square)] = PLAYER_MARK


def computer_choice(board):
    options = empty_squares(board)
    if options:
        square = random.choice(options)
        board[square] = COMPUTER_MARK
    return 


def check_for_winner(board):
    player_state = {key
                    for key, value in board.items()
                    if value == PLAYER_MARK}
    computer_state = {key
                      for key, value in board.items()
                      if value == COMPUTER_MARK}
    
    for condition in WIN_CONDITIONS:
        if player_state >= condition:
            return 'User wins!'
        elif computer_state >= condition:
            return 'Computer wins!'


def play_tic_tac_toe():
    while True:
        board = initialize_board()

        while True:
            display_board(board)

            player_choice(board)
            if check_for_winner(board) or not empty_squares(board):
                break

            computer_choice(board)
            if check_for_winner(board) or not empty_squares(board):
                break
        
        display_board(board)

        if check_for_winner(board):
            prompt(check_for_winner(board))
        else:
            prompt("It's a draw!")
        
        prompt('Continue playing? Enter y or n')
        answer = input()
        if answer[0] not in {'y', 'Y'}:
            break

    prompt("Thanks for playing!")

play_tic_tac_toe()