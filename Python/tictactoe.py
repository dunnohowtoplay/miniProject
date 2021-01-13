import random

board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]

game_running = True

# board condition


def board_condition():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

# npc turn
def npc():
    global game_running
    arr = []
    for x in range(len(board)):
        if board[x] == '-':
            arr.append(x)
    if len(arr) == 0:
        game_running = False
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


def check_winner():
    # win => all winning possibility
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    # Draw
    if '-' not in board:
        return 'D'

    for x in win:
        # X win condition
        if all(board[y] == 'X' for y in x):
            return 'X'
        # O win condition
        if all(board[y] == 'O' for y in x):
            return 'O'

#start the game
def start_game():
    global game_running
    while game_running:
        board_condition()
        controller()
        if check_winner() == 'X':
            board_condition()
            print('X Win!')
            game_running = False
        if check_winner() == 'O':
            board_condition()
            print('O Win!')
            game_running = False
        if check_winner() == 'D':
            board_condition()
            print('Draw')
            game_running = False
        npc()

#reset game board        
def reset():
    for x in range(len(board)):
        board[x] = '-'


while True:
    if game_running == True:
        start_game()
    else:
        ask = input('Play Again ? (y/n)')
        while ask not in ('yYnN') or ask == '':
            ask = input('Invalid input, Play Again ? (y/n)')

        if ask in ('yY'):
            game_running = True
            reset()
            start_game()
        else:
            break
