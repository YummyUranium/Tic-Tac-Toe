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

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0
    gameWon = False


    while gameWon == False:
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

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ' or board['4'] == board['5'] == board['6'] != ' ' or board['1'] == board['2'] == board['3'] != ' ' or board['1'] == board['4'] == board['7'] != ' ' or board['2'] == board['5'] == board['8'] != ' ' or board['3'] == board['6'] == board['9'] != ' ' or board['7'] == board['5'] == board['3'] != ' ' or board['1'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame over. " + turn + " won!")
                gameWon = True
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play again?\nPress 'Y' for yes, 'N' for no: ")
    if restart == "y" or restart == "Y":
        print("Restarting...")
        for key in board_keys:
            board[key] = " "
    elif restart == "n" or restart == "N":
        quit()
    game()

if __name__ == "__main__":
    game()