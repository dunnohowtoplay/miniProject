import random

board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]

# board condition


def board_condition():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

# npc turn
def npc():
    #global game_running
    arr = []
    for x in range(len(board)):
        if board[x] == '-':
            arr.append(x)
    if len(arr) == 0:
        return False
    else:
        board[random.choice(arr)] = 'O'


# game controller
def controller():
    pos = input("Choose position (1-9): ")
    while pos not in ('123456789') or pos == '':
        pos = input("Invalid input, Choose position (1-9): ")
    while board[int(pos)-1] != '-':
        pos = input("Already taken, Choose another position (1-9): ")

    board[int(pos)-1] = 'X'

# winning condition
def win_condition():
    # win => all winning possibility
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for x in win:
        # X win condition
        if all(board[y] == 'X' for y in x):
            return 'X'
        # O win condition
        if all(board[y] == 'O' for y in x):
            return 'O'
        # Draw
        if not(all(board[y] == 'X' for y in x) and all(board[y] == 'O' for y in x)) and '-' not in board:
            return 'D'

#check winner
def check_winner():
    if win_condition() == 'X':
        board_condition()
        print('X Win!')
        return False
    elif win_condition() == 'O':
        board_condition()
        print('O Win!')
        return False
    elif win_condition() == 'D':
        board_condition()
        print('Draw')
        return False
    else:
        return True


#start the game
def start_game():
    while True:
        board_condition()
        if check_winner() == False:
            break
        controller()
        if check_winner() == False:
            break
        if npc() == False:
            break
        if check_winner() == False:
            break
        
        

#reset game board        
def reset():
    for x in range(len(board)):
        board[x] = '-'


while True:
    start_game()
    ask = input('Play Again ? (y/n)')
    while ask not in ('yYnN') or ask == '':
        ask = input('Invalid input, Play Again ? (y/n)')

    if ask in ('yY'):
        reset()
    else:
        break
