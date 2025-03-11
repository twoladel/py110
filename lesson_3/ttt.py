import os
import random

EMPTY_SQUARE = ' '
PLAYER_MARK = 'X'
COMPUTER_MARK = '0'
WIN_CONDITIONS = [
    [1, 2, 3],
    [1, 4, 7],
    [1, 5, 9],
    [4, 5, 6],
    [7, 8, 9],
    [2, 5, 8],
    [3, 6, 9],
    [3, 5, 7]
]
MATCH_WIN = 5


def initialize_board():
    return {num: ' ' for num in range(1, 10)}


def display_board(board):
    os.system('clear')
    print(f'You are {PLAYER_MARK}. The Computer is {COMPUTER_MARK}.')
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


def user_board(board):
    return [key for key, value in board.items() if value == PLAYER_MARK]

def computer_board(board):
    return [key for key, value in board.items() if value == COMPUTER_MARK]


def join_or(lst, delimiter=', ', joining_word='or'):
    if len(lst) == 2:
        return f'{lst[0]} {joining_word} {lst[1]}'
    elif len(lst) > 2:
        choices = delimiter.join(lst[0:-1])
        return f'{choices}{delimiter}{joining_word} {lst[-1]}'
    
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
    if not options:
        return 
    
    computer_state = computer_board(board)
    if find_move(computer_state, options):
        square = find_move(computer_state, options)
        board[square] = COMPUTER_MARK
        return
    
    user_state = user_board(board)
    if find_move(user_state, options):
        square = find_move(user_state, options)
        board[square] = COMPUTER_MARK
        return 
            
    square = random.choice(options)
    board[square] = COMPUTER_MARK


def find_move(player_state, options):
    for win in WIN_CONDITIONS:
        square = find_square(win, player_state)
        print(square)

        if square and square in options:
            return square

    return 

def find_square(win, player_state):
    analyzer = []
    for key in player_state:
        if key in win:
            analyzer.append(key)
        if len(analyzer) == 2:
            missing_square = set(win) - set(analyzer)
            return missing_square.pop()

def check_for_winner(board):
    for condition in WIN_CONDITIONS:
        s1, s2, s3 = condition
        if (board[s1] == PLAYER_MARK
            and board[s2] == PLAYER_MARK
            and board[s3] == PLAYER_MARK):
            return 'You'
        elif (board[s1] == COMPUTER_MARK
              and board[s2] == COMPUTER_MARK
              and board[s3] == COMPUTER_MARK):
            return 'Computer'
    
    return None


def update_score(score, winner):
    score[winner] += 1


def display_score(score):
    prompt("Scoreboard")
    for key, value in score.items():
        print(f'{key}: {value}')


def detect_match_winner(score):
    for player, wins in score.items():
        if wins == MATCH_WIN:
            return player
        return None
    
def keep_playing(message):
    prompt(f'{message}? y or n')
    answer = input()
    if answer[0] in {'y', 'Y'}:
        return True
    return False

def play_tic_tac_toe():
    while True:
        score = {'You': 0, 'Computer': 0}

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
                winner = check_for_winner(board)
                prompt(f'{winner} won!')
                update_score(score, winner)
                display_score(score)
            else:
                prompt("It's a draw!")
                display_score(score)

            if detect_match_winner(score):
                prompt(f'{detect_match_winner(score)} won the match!')
                break

            if not keep_playing('Continue playing'):
                break
        
        if not keep_playing('Another match'):
            break

    prompt("Thanks for playing!")

play_tic_tac_toe()