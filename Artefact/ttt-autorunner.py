# Original game from https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874
# Altered a lot.
# Game is played in the console.

import random

import csv

header = ["Game Number", "Gamemode", "Result", "Winner", "Game Length", "Starting Cell", "Final Board State"]

with open("./Artefact/ttt-data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)

game_number = 1

def log_data(game_number, gamemode, result, winner, game_length, starting_cell, final_board_state):
    with open("./Artefact/ttt-data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        data_to_log = [game_number, gamemode, result, winner, game_length, starting_cell, final_board_state]
        writer.writerow(data_to_log)

# The board is represented with a dictionary and corresponding cell numbers
board = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in board:
    board_keys.append(key)

# For logging the final board state
def stringify_board(board):
    board_string = []
    for key in board_keys:
        board_string.append(board[key])
    return board_string

# Resets the board state
def restart_board():
    for key in board_keys:
            board[key] = " "

# Checks if the game has been won
def is_game_won(boardstate=list):
    if boardstate['7'] == boardstate['8'] == boardstate['9'] == "X" or boardstate['4'] == boardstate['5'] == boardstate['6'] == "X" or boardstate['1'] == boardstate['2'] == boardstate['3'] == "X" or boardstate['1'] == boardstate['4'] == boardstate['7'] == "X" or boardstate['2'] == boardstate['5'] == boardstate['8'] == "X" or boardstate['3'] == boardstate['6'] == boardstate['9'] == "X" or boardstate['7'] == boardstate['5'] == boardstate['3'] == "X" or boardstate['1'] == boardstate['5'] == boardstate['9'] == "X":
        return "X", "Done"
    elif boardstate['7'] == boardstate['8'] == boardstate['9'] == "O" or boardstate['4'] == boardstate['5'] == boardstate['6'] == "O" or boardstate['1'] == boardstate['2'] == boardstate['3'] == "O" or boardstate['1'] == boardstate['4'] == boardstate['7'] == "O" or boardstate['2'] == boardstate['5'] == boardstate['8'] == "O" or boardstate['3'] == boardstate['6'] == boardstate['9'] == "O" or boardstate['7'] == boardstate['5'] == boardstate['3'] == "O" or boardstate['1'] == boardstate['5'] == boardstate['9'] != ' ':
        return "O", "Done"
    elif is_game_full(boardstate) == True:
        return None, "Draw"
    else:
        return None, "Not Done"

# Checks if the game is drawed
def is_game_full(boardstate=list):
    for key in boardstate:
        if boardstate[key] == " ":
            return False
    return True
    
# Changes the player
def change_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'  

# Returns an array of empty cells left
def get_possible_moves(boardstate=list):
    possible_moves = []
    for key in boardstate:
        if boardstate[key] == ' ':
            possible_moves.append(key)
    return possible_moves

# Starts the game loop
def start_game():

    global game_number

    # Asks the user for a cell number, rejects invalid inputs
    while True:
        try:
            runs = int(input("How many times would you like to run the program?\nRuns: "))
            if runs <= 0:
                print("Sorry, the amount entered must be positive!")
                continue
        except ValueError:
            print("Sorry, you must enter a valid integer")
            continue
        else:
            break

    print("Running...")

    for game in range(runs):
        play_simulation_game()
        game_number = game + 2

    print("Done!")


def play_simulation_game():

    result = None
    winner = None
    starting_cell = None
    turn = 'X'
    count = 0
    game_over = False
    while game_over == False:

        if count == 0:
            board["2"] = turn
            starting_cell = 2
        else:
            # The computer selects a random square, and then places it's symbol in it.
            random_square = random.choice(get_possible_moves(board))
            board[str(random_square)] = turn

        # Checks if the game is finished 
        if is_game_won(board)[1] == "Done":
            result = "Winner"
            winner = turn
            game_over = True
            log_data(game_number, ("Simulation Play", "Random"), result, winner, (count + 1), starting_cell, stringify_board(board))
            restart_board()
            break
        elif is_game_won(board)[1] == "Draw":
            result = "Draw"
            winner = "None"
            game_over = True
            log_data(game_number, ("Simulation Play", "Random"), result, winner, (count + 1), starting_cell, stringify_board(board))
            restart_board()
            break

        turn = change_player(turn)

        count += 1

if __name__ == "__main__":
    start_game()