# Game from https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874

# The board is represented with a dictionary and corresponding cell numbers

board = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in board:
    board_keys.append(key)

# Prints the current board state
def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('― + ― + ―')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('― + ― + ―')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

def start_game():
    print("Let's play Tic-Tac-Toe!")
    print("What gamemode would you like to play?")

    while True:
        try:
            gamemode_selected = int(input("Please enter 1 for singleplayer (human against computer), 2 for multiplayer (human against human), or 3 for simulation play (computer against computer): "))
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
    print("Sorry, this functionality hasn't been added yet!")
    quit()

# The main function which has all the singleplayer gameplay functionality.
def play_multiplayer_game():

    turn = 'X'
    count = 0
    gameOver = False


    while gameOver == False:
        printBoard(board)
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

        # Now we will check if player X or O has won, for every move after 5 moves. 
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ' or board['4'] == board['5'] == board['6'] != ' ' or board['1'] == board['2'] == board['3'] != ' ' or board['1'] == board['4'] == board['7'] != ' ' or board['2'] == board['5'] == board['8'] != ' ' or board['3'] == board['6'] == board['9'] != ' ' or board['7'] == board['5'] == board['3'] != ' ' or board['1'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame over. " + turn + " won!")
                gameOver = True
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a tie!")
            restart_board()
            break

        # Changes the player
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Asks if player wants to restart the game or not.
    restart = input("Do want to play again?\nPress 'Y' for yes, 'N' for no: ")
    if restart == "y" or restart == "Y":
        print("Restarting...")
        restart_board()
    elif restart == "n" or restart == "N":
        quit()
    start_game()

def play_simulation_game():
    print("Sorry, this functionality hasn't been added yet!")
    quit()

def restart_board():
    for key in board_keys:
            board[key] = " "

if __name__ == "__main__":
    start_game()