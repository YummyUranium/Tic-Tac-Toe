# Game from https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874

# The board is represented with a dictionary and corresponding cell numbers

board = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in board:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('- + - + -')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('- + - + -')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(board)
        print("It's your turn, " + turn + ". Where would you like to place your symbol?")

        move = input()        

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ' or board['4'] == board['5'] == board['6'] != ' ' or board['1'] == board['2'] == board['3'] != ' ' or board['1'] == board['4'] == board['7'] != ' ' or board['2'] == board['5'] == board['8'] != ' ' or board['3'] == board['6'] == board['9'] != ' ' or board['7'] == board['5'] == board['3'] != ' ' or board['1'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame over. " + turn + " won!")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            board[key] = " "

        game()

if __name__ == "__main__":
    game()