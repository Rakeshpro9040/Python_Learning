# import os
from IPython.display import clear_output
import random

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

# player_board = ['']*9
# print(player_board)
# display_board(player_board)

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
    marker1 = input('''Player 1, please enter 'X' or 'O': ''')
    while marker1 not in ('X', 'O'):
        print('Wrong marker!!!')
        marker1 = input('''Player 1, please enter 'X' or 'O': ''')
    if marker1 == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'
    return marker1, marker2  # Return a Tuple here, so that later we can use Tuple Unpacking

# (player1_marker,player2_marker) = player_marker() # Tuple Unpacking
# print('player1_marker: '+player1_marker)
# print('player2_marker: '+player2_marker)

"""
Step 2_2:
Accept Position in board
"""
def player_position():
    position = input('''Please enter position, Enter (1,9): ''')
    accepted_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while (position.isdigit() == False) or (position not in accepted_values):
        if not position.isdigit():
            print('Number is expected in Position not Char, Retry!!!')
        elif position not in accepted_values:
            print('Enter a number between 1 to 9, Retry!!!')
        position = input('''Please enter position, Enter (1,9): ''')
    return int(position)


# player1_position = player_position()
# print('player1_position: '+ str(player1_position))

"""
Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
"""
def player_position_assign(board,marker,position):
    board[position-1] = marker

# player_position_assign(player_board,player1_marker,player1_position)
# display_board(player_board)

'''
Step 4: run the win_check function against our player_board - it should return True
'''
def player_win_check(board,marker):
    for i in [1,2,3,4]: # 1 is for horizontal; 3 is for vertical; 2 is for left diagonal, 4 is for right diagonal
        if i == 1:
            for j in [0,3,6]:
                if board[j] == board[j+1] == board[j+2] == marker: # for horizontal add 1
                    return True
        if i == 4:
            if board[0] == board[4] == board[8] == marker: # for right diagonal add 4
                    return True
        if i == 2:
            if board[2] == board[4] == board[6] == marker: # for right diagonal add 2
                    return True
        if i == 3:
            for j in [0,1,2]:
                if board[j] == board[j+3] == board[j+6] == marker: # for vertical add 3
                    return True
    return False

# player_board = ['1','1','1','1','1','1','0','1','']
# display_board(player_board)
# print(player_win_check (player_board,'1'))

'''
Step 5: Write a function that uses the random module to randomly decide which player goes first. 
You may want to lookup random.randint() Return a string of which player went first.
'''

def random_player_chose():
    x = random.randint(0, 1)
    if x == 1:
        return 'Player 1'
    else:
        return 'Player 2'

'''
Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
'''
def board_space_check(board, position):
    return board[position] == ''

# print(board_space_check(player_board,2))

'''
Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
'''
def full_board_check(board):
    for i,val in enumerate(board):
        if val == '':
            return False
    return True

# print(full_board_check(player_board))

'''
Step 8: Write a function that asks for a player's next position (as a number 1-9) 
and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
'''
def player_position_with_space_check(board):
    position = player_position()
    while not board_space_check(board,position-1):
        print('Space is already taken, Retry!!!')
        position = player_position()
    return position

# print(player_position_sec(player_board))

'''
Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
'''
def replay():
    result = input("Want to Replay this game, Enter 'Y' or 'N': ")
    if result == 'Y':
     return True
    else:
        return False

# print(replay())

'''
Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
'''
print('Welcome to Tic Tac Toe!')

while True:

    # Setup board
    player_board = [''] * 9
    display_board(player_board)
    game_on = not full_board_check(player_board)

    # Define player-1, player-2 Marker
    player1_marker, player2_marker = player_marker()
    print('Player1 Marker: ' + player1_marker)
    print('Player2 Marker: ' + player2_marker)

    # Call Rand function here for turn

    while game_on:

        # Player-1's Turn
        print("Player 1's Turn")
        player1_position = player_position_with_space_check(player_board)
        player_position_assign(player_board,player1_marker,player1_position)
        if player_win_check(player_board, player1_marker):
            game_result = 'Player 1 has WON!!!'
            print('Game Result: ' + game_result)
            break
        print("Player 1's Result")
        display_board(player_board)

        if full_board_check(player_board):
            game_result = "It's a Tie!!!"
            print('Game Result: ' + game_result)
            break

        # Player-2's Turn
        print("Player 2's Turn")
        player2_position = player_position_with_space_check(player_board)
        player_position_assign(player_board,player2_marker,player2_position)
        if player_win_check(player_board, player2_marker):
            game_result = 'Player 2 has WON!!!'
            print('Game Result: ' + game_result)
            break
        print("Player 2's Result")
        display_board(player_board)

        # Check Full board
        if full_board_check(player_board):
            game_result = "It's a Tie"
            print('Game Result: ' + game_result)
            break
        else:
            game_on == True

    if not replay():
        break

display_board(player_board)