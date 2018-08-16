from IPython.display import clear_output
from random import randint

import random
player_1_marker = ""
player_2_marker = ""
game_cancelled = False
def display_board(board = ["#", "O", "X", "X", "O", "O", "X", "X", "O", "#"]):
    clear_output()
    print(f"    |     |    ")
    print(f" {board[1]}  |  {board[2]}  |  {board[3]} ")
    print(f"    |     |    ")
    print(f"---------------")
    print(f"    |     |    ")
    print(f" {board[4]}  |  {board[5]}  |  {board[6]} ")
    print(f"    |     |    ")
    print(f"---------------")
    print(f"    |     |    ")
    print(f" {board[7]}  |  {board[8]}  |  {board[9]} ")
    print(f"    |     |    ")

def pick_marker():
    keep_asking = True
    while(keep_asking):
        player_1_marker = input("Player 1, pick a marker 'X' or 'O' (enter 'E' to Exit)")
        player_1_marker = player_1_marker.upper()
        if player_1_marker == "O" or player_1_marker == "X":
            keep_asking = False
        if player_1_marker == "E":
            keep_asking = False
            game_cancelled = True
        clear_output()
    if player_1_marker == "O":
        player_2_marker = "X"
    elif player_1_marker == "X":
        player_2_marker = "O"
    print(f'Player 1 selected {player_1_marker}')
    return { 1: player_1_marker , 2: player_2_marker}
    
def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, mark):
    return board[1] == board[2] == board[3] == mark \
    or board[1] == board[4] == board[7] == mark \
    or board[1] == board[5] == board[9] == mark \
    or board[2] == board[5] == board[8] == mark \
    or board[3] == board[6] == board[9] == mark \
    or board[3] == board[5] == board[7] == mark \
    or board[4] == board[5] == board[6] == mark \
    or board[7] == board[8] == board[9] == mark

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return not ' ' in board

def choose_first():
    first = randint(1, 2)
    print(f"Player {first} goes first.")
    return first

def replay():
    replay = input("Do you want to play again? (Y or N)")
    replay = replay.lower()
    if replay == 'y':
        return True
    if replay == 'n':
        return False
            
def player_choice(board):
    supplied_input = input("Choose your next position (1 - 9): ")
    try:
        int(supplied_input)
        pass
    except:
        return -1
    choice = int(supplied_input)
    if choice in range(1, 10):
        if space_check(board, choice):
            return choice
        else:
            return -1

def start_game():
    print('Welcome to Tic Tac Toe!')
    player_markers = pick_marker()
    game_on = True
    first_player = choose_first()
    game_board = ["X", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    display_board(game_board)
    print("Markers" ,player_markers)
    current_player = first_player
    while True:
        while game_on:
            print(f"Player {current_player}'s turn: ")
            choice_position = player_choice(game_board)
            if choice_position != -1:
                current_player_symbol = player_markers[current_player]
                game_board = place_marker(game_board, current_player_symbol, choice_position)
                display_board(game_board)
                print('Got here')
                if win_check(game_board, current_player_symbol):
                    print(f"Player {current_player} has won the game!")
                    break
                if full_board_check(game_board):
                    print("Nobody won this round.")
                    break
                current_player = (current_player % 2) + 1
            else:
                print("That position is filled. Pick another.")
        if not replay():
            break
        else:
            start_game()

        
        
#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break