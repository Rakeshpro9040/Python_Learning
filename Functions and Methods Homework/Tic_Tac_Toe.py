import os
from IPython.display import clear_output

"""
Step 1: Write a function that can print out a board. Set up your board as a list,
where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
"""
# clear = lambda : os.system('cls')

def display_board(board):
    clear_output()
    print('_'*10)
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')

    print('_'*10)
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('_'*10)

    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('_'*10)

player_board = ['']*9
# print(player_board)

display_board(player_board)

"""
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
Think about using while loops to continually ask until you get a correct answer
"""
# clear_output()
# print('\n'*100)

"""
Step 2_1:
Accept Markers
"""

def player_marker():
    player1 = input('''Player 1, please enter 'X' or 'O': ''')
    while player1 not in ('X', 'O'):
        player1 = input('''Player 1, please enter 'X' or 'O': ''')
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player1,player2 # Return a Tuple here, so that later we can use Tuple Unpacking

(player1_marker,player2_marker) = player_marker() # Tuple Unpacking
print('player1_marker: '+player1_marker)
print('player2_marker: '+player2_marker)

"""
Step 2_2:
Accept Position in board
"""

def player_position():
    player = input('''Player 1, please enter position, Enter (1,9): ''')
    accepted_values = ['1','2','3','4','5','6','7','8','9']
    while (player.isdigit() == False) or (player not in accepted_values):
        if not player.isdigit():
            print('Number is expected in Position not Char, Retry!!!')
        elif player not in accepted_values:
            print('Enter a number between 1 to 9, Retry!!!')
        player = input('''Player 1, please enter position, Enter (1,9): ''')
    return int(player)

player1_position = player_position()
print('player1_position: '+ str(player1_position))

"""
Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
"""
def player_position_assign(board,marker,position):
    board[position-1] = marker

player_position_assign(player_board,player1_marker,player1_position)
display_board(player_board)

'''
TEST Step 4: run the win_check function against our player_board - it should return True
'''

def player_win_check(board,marker):
    result = False
    for i in [1,2,3,4]: # 1 is for horizontal; 3 is for vertical; 2 is for left cross, 4 is for right cross
        if i == 1:
            for j in [0,3,6]:
                if board[j] == board[j+1] == board[j+2] == marker: # for horizontal add 1
                    result = True
        if i == 4:
            if board[0] == board[4] == board[8] == marker: # for right cross add 4
                    result = True
        if i == 2:
            if board[2] == board[4] == board[6] == marker: # for right cross add 2
                    result = True
        if i == 3:
            for j in [0,1,2]:
                if board[j] == board[j+3] == board[j+6] == marker: # for vertical add 3
                    result = True
    return result

player_board = ['1','1','1','1','1','1','0','1','']
display_board(player_board)
# print(player_win_check (player_board,'1'))

'''
Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
'''

def board_space_check(board, position):
    result = True
    if board[position] != '':
        result = False
    return result

# print(board_space_check(player_board,2))

'''
Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
'''
def full_board_check(board):
    result = True
    for i,val in enumerate(board):
        if val == '':
            result = False
            break
    return result

print(full_board_check(player_board))