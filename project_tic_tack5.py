#DisPlaY THE BOARD

def display_board(board):
    print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])


tack_board = [' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ']


def player_input():
    '''
    OUTPUT: (Player 1 marker, Player 2 marker)
    '''
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

#tuple unpacking
# player1_marker, player2_marker = player_input()
# print(f"Player 1: {player1_marker}, Player 2: {player2_marker}")

#TAKE MARKER AND ASSIGN TO BOARD AT A POSITION
def place_marker(board, marker, position):
    board[position] = marker

#4 TAKES A BOARD AND A MARK (X OR O) AND CHECK TO SEE IF THAT MARK HAS WON.
def win_check(board, mark):
    #WIN TIC TACK TOE
    #All rows have same marker
    return (
        (tack_board[7] == mark and tack_board[8] == mark and tack_board[9]) or
         
        (tack_board[4] == mark and tack_board[5] == mark and tack_board[6]) or
           
        (tack_board[1] == mark and tack_board[2] == mark and tack_board[3]) or
           
#columns
        (tack_board[1] == mark and tack_board[4] == mark and tack_board[7]) or
           
        (tack_board[2] == mark and tack_board[5] == mark and tack_board[8]) or
          
        (tack_board[3] == mark and tack_board[6] == mark and tack_board[9]) or
#Two diagonals
        (tack_board[1] == mark and tack_board[5] == mark and tack_board[9]) or 
        (tack_board[3] == mark and tack_board[5] == mark and tack_board[7])
           )
   

# USE RANDOM MODULE TO DECIDE WHICH PLAYER GOES FIRST.
import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#Return Boolean for space available
def space_check(board, position):
   return board[position] == ' '

#REturn boolean for full board available
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    #Board is full if we return True
        else:
            return True

#STEP 8 ASK FOR PLAYER'S NEXT POSITION (1-9)
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose a position: (1-9): "))

    return position

#STEP 9 Ask player to play again
def replay():
    choice = input("Play again: Yes or No ")
    return choice == 'Yes'

#STEP 10 PUT IT ALL TOGETHER

# WHILE LOOP TO KEEP RUNNING THE GAME
print("Welcome to Tic Tac Toe!\n")

while True:
    #play the game
    ##Set up Board, who is first, choose markers X , O
    # tack_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to to play? y or n: ')
    if play_game =='y':
        game_on = True
    else:
        game_on = False
    ## GAME PLAY
    while game_on:
        if turn == 'Player 1':
            #SHOW BOARD
            display_board(tack_board)
            #Choose a position
            position = player_choice(tack_board)
            #Place marker on position
            place_marker(tack_board,player1_marker,position)
            # Check if they won
            if win_check(tack_board,player1_marker):
                display_board(tack_board)
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check(tack_board):
                    display_board(tack_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            
            display_board(tack_board)
            #Choose a position
            position = player_choice(tack_board)
            #Place marker on position
            place_marker(tack_board,player2_marker,position)
            # Check if they won
            if win_check(tack_board,player2_marker):
                display_board(tack_board)
                print('Player 2 has won')
                game_on = False
            else:
                if full_board_check(tack_board):
                    display_board(tack_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 1'

    ### Player one turn 

        

    ##Player two turn 


    if not replay():
        break

#BREAK OUT OF THE WHILE LOOP ON REPLAY