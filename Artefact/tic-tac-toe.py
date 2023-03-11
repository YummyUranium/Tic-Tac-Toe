# Original game from https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874
# Altered a lot.
# Game is played in the console.

import random
import math
import time

players = ["X", "O"]

# The board is represented with a dictionary and corresponding cell numbers
board = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in board:
    board_keys.append(key)

# Prints the current board state
def print_board(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('― + ― + ―')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('― + ― + ―')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

# Resets the board state
def restart_board():
    for key in board_keys:
            board[key] = " "

def ask_to_restart():
    while True:
        # Asks if player wants to restart the game or not.
        restart = input("Do want to play again?\nPress 'Y' for yes, 'N' for no: ")
        if restart == "y" or restart == "Y":
            print("Restarting...")
            restart_board()
            start_game()
        elif restart == "n" or restart == "N":
            quit()
        else:
            print("Sorry, no valid input was given.")
            continue

# Checks if the game has been won
def is_game_won(boardstate=list):
    if boardstate['7'] == boardstate['8'] == boardstate['9'] == "X" or boardstate['4'] == boardstate['5'] == boardstate['6'] == "X" or boardstate['1'] == boardstate['2'] == boardstate['3'] == "X" or boardstate['1'] == boardstate['4'] == boardstate['7'] == "X" or boardstate['2'] == boardstate['5'] == boardstate['8'] == "X" or boardstate['3'] == boardstate['6'] == boardstate['9'] == "X" or boardstate['7'] == boardstate['5'] == boardstate['3'] == "X" or boardstate['1'] == boardstate['5'] == boardstate['9'] == "X":
        return True, "X"
    elif boardstate['7'] == boardstate['8'] == boardstate['9'] == "O" or boardstate['4'] == boardstate['5'] == boardstate['6'] == "O" or boardstate['1'] == boardstate['2'] == boardstate['3'] == "O" or boardstate['1'] == boardstate['4'] == boardstate['7'] == "O" or boardstate['2'] == boardstate['5'] == boardstate['8'] == "O" or boardstate['3'] == boardstate['6'] == boardstate['9'] == "O" or boardstate['7'] == boardstate['5'] == boardstate['3'] == "O" or boardstate['1'] == boardstate['5'] == boardstate['9'] != ' ':
        return True, "O"
    else:
        return False, None

# Checks if the game is drawed
def is_game_draw(boardstate=list):
    if not is_game_won(boardstate) and not get_possible_moves(boardstate):
        return True
    else:
        return False
    
# Changes the player
def change_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'  

# Returns an array of empty cells left
def get_possible_moves(boardstate=list):
    possible_moves = []
    for key in boardstate:
        if boardstate[key] == ' ':
            possible_moves.append(key)
    return possible_moves

def sim_move(boardstate=list, player=str, cell=int):
    boardstate[int(cell) - 1] = player

# MINIMAX ALGORITHM YAY
def get_best_move(boardstate=list, player=str, current_player=str):
    if is_game_won(boardstate)[1] == player and is_game_won(boardstate)[0] == True:
        return (1, 0)
    elif is_game_won(boardstate)[1] != player and is_game_won(boardstate)[0] == True:
        return (-1, 0)
    elif is_game_draw(boardstate):
        return (0, 0)

    moves = []
    possible_moves = get_possible_moves(boardstate)

    for possible_move in possible_moves:
        move = {}
        move["index"] = possible_move
        new_state = copy_game_state(boardstate)
        sim_move(new_state, player, possible_move)

        # i dont understand this at all wtf
        if player == current_player:
            result,_ = get_best_move(new_state, change_player(player))
            move["score"] = result
        else:
            result,_ = get_best_move(new_state, player)
            move['score'] = result
        
        moves.append(move)
        
    # Find best move
    best_move = None
    if player == current_player:
        best = -math.inf
        for move in moves:
            if move["score"] > best:
                best = move["score"]
                best_move = move["index"]
    else:
        best = math.inf
        for move in moves:
            if move['score'] < best:
                best = move['score']
                best_move = move['index']
    
    return (best, best_move)

def copy_game_state(boardstate=list):
    new_state = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
    for key in board_keys:
        new_state[key] = boardstate[key]
    return new_state

# Starts the game loop
def start_game():
    print("Let's play Tic-Tac-Toe!")
    print("What gamemode would you like to play?")

    while True:
        try:
            gamemode_selected = int(input("Please enter:\n1 for singleplayer (human against computer)\n2 for multiplayer (human against human)\n3 for simulation play (computer against computer): "))
        except ValueError:
            print("Sorry, you must enter 1, 2 or 3.")
            continue
        if gamemode_selected not in range(1, 4):
            print("Sorry, you must enter 1, 2 or 3.")
            continue
        else:
            break
    
    if gamemode_selected == 1:
        play_singleplayer_game()
    elif gamemode_selected == 2:
        play_multiplayer_game()
    elif gamemode_selected == 3:
        play_simulation_game()
    else:
        print("Something has gone terribly wrong in the checking of what gamemode was selected...")

def play_singleplayer_game():

    while True:
        difficulty_selected = int(input("Please enter the difficulty you want:\n1 for Easy (the computer's moves are randomly selected)\n2 for Impossible (the computer will always select the optimal move): "))
        if difficulty_selected == 1 or difficulty_selected == 2:
            break
        else:
            print("Sorry, please enter 1 or 2")
            continue
    
    turn = "X"
    count = 0
    game_over = False

    while game_over == False:
        # Random moves from computer
        if difficulty_selected == 1:
            print_board(board)
            print("It's your turn. Where would you like to place your symbol?")

            # Checks if player X or O has won, for every move after 5 moves. 
            if count >= 5:
                if is_game_won(board) == True:
                    print_board(board)
                    print("\nGame over. O won!\n")
                    game_over = True
                    break
                
            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if is_game_draw():
                print("\nGame Over.\n")                
                print("It's a tie!")
                restart_board()
                break

            # Asks the user for a cell number, rejects invalid inputs
            while True:
                try:
                    move = int(input("Cell number: "))
                except ValueError:
                    print("Sorry, you must enter a valid cell number (a number between 1 and 9)")
                    continue
                if move not in range(1, 10):
                    print("Sorry, you must enter a valid cell number (a number between 1 and 9)")
                    continue
                else:
                    break
            
            # Checks if the chosen cell is empty, adds the symbol if it is.
            if board[str(move)] == ' ':
                board[str(move)] = turn
                count += 1
            else:
                print("Sorry, that place is already filled.")
                continue

            # Checks if player X or O has won, for every move after 5 moves. 
            if count >= 5:
                if is_game_won(board):
                    print_board(board)
                    print("\nGame over. X won!")
                    game_over = True
                    break

            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if is_game_draw():
                print("\nGame Over.\n")                
                print("It's a tie!")
                restart_board()
                break

            # The computer selects a random square, checks if it's filled, and then places an 'O' in it.
            while True:
                random_square = random.choice(get_possible_moves(board))
                # Checks if the chosen cell is empty, adds the symbol if it is.
                if board[str(random_square)] == ' ':
                    board[str(random_square)] = "O"
                    count += 1
                    break
                else:
                    continue

        # The computer's moves are impossible to win against
        elif difficulty_selected == 2:
            print("Sorry, this functionality hasn't been added yet.")
            start_game()
        else:
            print("Something has gone terribly wrong processing the difficulty selection")
        
    ask_to_restart()

# The main function which has all the singleplayer gameplay functionality.
def play_multiplayer_game():

    turn = 'X'
    count = 0
    game_over = False

    while game_over == False:
        print_board(board)
        print("It's your turn, " + turn + ". Where would you like to place your symbol?")

        # Asks the user for a cell number, rejects invalid inputs
        while True:
            try:
                move = int(input("Cell number: "))
            except ValueError:
                print("Sorry, you must enter a valid cell number (a number between 1 and 9)")
                continue
            if move not in range(1, 10):
                print("Sorry, you must enter a valid cell number (a number between 1 and 9)")
                continue
            else:
                break

        # Checks if the chosen cell is empty, adds the symbol if it is.
        if board[str(move)] == ' ':
            board[str(move)] = turn
            count += 1
        else:
            print("Sorry, that place is already filled.")
            continue

        # Checks if player X or O has won, for every move after 5 moves. 
        if count >= 5:
            if is_game_won(board):
                print_board(board)
                print("\nGame over. " + turn + " won!")
                game_over = True
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if is_game_draw():
            print("\nGame Over.\n")                
            print("It's a tie!")
            restart_board()
            break

        change_player(turn)       
    
    ask_to_restart()


def play_simulation_game():

    while True:
        mode_selected = int(input("Please enter the mode you want:\n1 for Random (the computer's moves are randomly selected)\n2 for Optimal (the computer will always select the optimal move): "))
        if mode_selected == 1 or mode_selected == 2:
            break
        else:
            print("Sorry, please enter 1 or 2")
            continue

    turn = 'X'
    count = 0
    game_over = False

    print_board(board)
    print("\n―――――――――\n")
    time.sleep(1)

    while game_over == False:
        if mode_selected == 1:
            print("It is " + turn + "'s turn.\n")
            # The computer selects a random square, and then places it's symbol in it.
            random_square = random.choice(get_possible_moves(board))
            board[str(random_square)] = turn

            print_board(board)

            # Checks if player X or O has won.
            if is_game_won(board):
                print("\nGame over. " + turn + " won!")
                game_over = True
                break

            # If neither X nor O wins and the board is full, we'll declare the result as a 'tie'.
            if is_game_draw():
                print("\nGame Over.\n")                
                print("It's a tie!")
                restart_board()
                break

            change_player(turn)

            time.sleep(1)
            count += 1
            print("\n―――――――――\n")
        elif mode_selected == 2:
            print("It is " + turn + "'s turn.\n")
            # The computer gets the best square
            _,best_square = get_best_move(board, turn, turn)
            board[str(best_square)] = turn
            print(board)
            print_board(board)

            # Checks if player X or O has won.
            if is_game_won(board):
                print("\nGame over. " + turn + " won!")
                game_over = True
                break

            # If neither X nor O wins and the board is full, we'll declare the result as a 'tie'.
            if is_game_draw():
                print("\nGame Over.\n")                
                print("It's a tie!")
                restart_board()
                break

            change_player(turn)

            time.sleep(1)
            count += 1
            print("\n―――――――――\n")
        else:
            print("Something has gone terribly wrong selecting simulation mode")
            quit()

    ask_to_restart()


if __name__ == "__main__":
    start_game()