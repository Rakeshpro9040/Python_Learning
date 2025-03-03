# Import Lib-Function
from random import shuffle

# Define shuffle_list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# Define player_guess
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Pick a number: 0,1, or 2: ')
    return int(guess)

# Define check_guess
def check_guess(mixedup_list,guess):
    if mylist[guess] == '0':
        print('Correct!')
    else:
        print('Wrong!')
        print(mixedup_list)

# Main Code
# INITIAL LIST
mylist = ['','0','']

# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(mixedup_list,guess)