board = {'TopL': ' ', 'TopM': ' ', 'TopR': ' ',
         'MidL': ' ', 'MidM': ' ', 'MidR': ' ',
         'BotL': ' ', 'BotM': ' ', 'BotR': ' '}
def printBoard(board):
    print(board['TopL'] + '|' + board['TopM'] + '|' + board['TopR'])
    print('_____')
    print(board['MidL'] + '|' + board['MidM'] + '|' + board['MidR'])
    print('_____')
    print(board['BotL'] + '|' + board['BotM'] + '|' + board['BotR'])
printBoard(board)   
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):
    print('Checking if ' + player + ' is a winner...')
    Top = {'TopL', 'TopM', 'TopR'}
    Mid = {'MidL', 'MidM', 'MidR'}
    Bot = {'BotL', 'BotM', 'BotR'}
    Left = {'TopL', 'MidL', 'BotL'}
    MidM = {'TopM', 'MidM', 'BotM'}
    Right = {'TopR', 'MidR', 'BotR'}
    TLBR = {'TopL', 'MidM', 'BotR'}
    BLTR = {'BotL', 'MidM', 'TopR'}
    if all(Top == X for i in range(9)):
        print('X WINS')
    if all(Mid == X for i in range(9)):
        print('X WINS')
    if all(Bot == X for i in range(9)):
        print('X WINS')
    if all(Left == X for i in range(9)):
        print('X WINS')
    if all(MidM == X for i in range(9)):
        print('X WINS')
    if all(Right == X for i in range(9)):
        print('X WINS')
    if all(TLBR == X for i in range(9)):
        print('X WINS')
    if all(BLTR == X for i in range(9)):
        print('X WINS')
    if all(Top == O for i in range(9)):
        print('O WINS')
    if all(Mid == O for i in range(9)):
        print('O WINS')
    if all(Bot == O for i in range(9)):
        print('O WINS')
    if all(Left == O for i in range(9)):
        print('O WINS')
    if all(MidM == O for i in range(9)):
        print('O WINS')
    if all(Right == O for i in range(9)):
        print('O WINS')
    if all(TLBR == O for i in range(9)):
        print('O WINS')
    if all(BLTR == O for i in range(9)):
        print('O WINS')
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
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
            print('O wins!') #Prins the win for O
            break #Breaks the loop
    
        if turn == 'X': #Checks to see if turn is equal to X
            turn = 'O' #If it isn't it sets it to O 
        else:
            turn = 'X' #It it is it sets it to X
        
    printBoard(board)
    
