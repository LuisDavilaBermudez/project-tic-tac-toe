board = {'TopL': ' ', 'TopM': ' ', 'TopR': ' ',
         'MidL': ' ', 'MidM': ' ', 'MidR': ' ',
         'BotL': ' ', 'BotM': ' ', 'BotR': ' '}
def printBoard(board):
    print(board['TopL'] + '|' + board['TopM'] + '|' + board['TopR'])
    print('_____')
    print(board['MidL'] + '|' + board['MidM'] + '|' + board['MidR'])
    print('_____')
    print(board['BotL'] + '|' + board['BotM'] + '|' + board['BotR'])  
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):
    print('Checking if ' + player + ' is a winner...')
    for i in range(9):
        if board['TopL'] and ['TopM'] and ['TopR'] == 'X':
            break
        if board['MidL'] and ['MidM'] and ['MidR'] == 'X':
            break
        if board['BotL'] and ['BotM'] and ['BotR'] == 'X':
            break
        if board['TopL'] and ['MidM'] and ['BotR'] == 'X':
            break
        if board['TopR'] and ['MidM'] and ['BotL'] == 'X':
            break
        if board['TopL'] and ['MidL'] and ['BotL'] == 'X':
            break
        if board['TopM'] and ['MidM'] and ['BotM'] == 'X':
            break
        if board['TopR'] and ['MidR'] and ['BotR'] == 'X':
            break
        if board['TopL'] and ['TopM'] and ['TopR'] == 'O':
            break
        if board['MidL'] and ['MidM'] and ['MidR'] == 'O':
            break
        if board['BotL'] and ['BotM'] and ['BotR'] == 'O':
            break
        if board['TopL'] and ['MidM'] and ['BotR'] == 'O':
            break
        if board['TopR'] and ['MidM'] and ['BotL'] == 'O':
            break
        if board['TopL'] and ['MidL'] and ['BotL'] == 'O':
            break
        if board['TopM'] and ['MidM'] and ['BotM'] == 'O':
            break
        if board['TopR'] and ['MidR'] and ['BotR'] == 'O':
            break
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board         #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9): #Uses a for loop to print the board at the start of a new turn
        printBoard(board)#It Prints the board
        print('Turn for ' + turn + '. Move on which space?') #It is telling the starting player to take a turn and which space to use.
        move = input() #It allows the player to put in their move
        board[move] = turn #It sets the move chosen
        if( checkWinner(board, 'X') ): #It checks to see if the paramaters for x as winner are present
            print('X wins!') #Prints The Win for X
            break #Breaks the loop
        elif ( checkWinner(board, 'O') ): #Checks for O winning parameters
            print('O wins!') #Prints the win for O
            break #Breaks the loop
    
        if turn == 'X': #Checks to see if turn is equal to X
            turn = 'O' #If it isn't it sets it to O 
        else:
            turn = 'X' #It it is it sets it to X
        
    printBoard(board)
    
