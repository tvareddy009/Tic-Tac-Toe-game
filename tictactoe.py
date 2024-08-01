import math

X = "X"
O = "O"
EMPTY = None
board= [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]   # intilizing the list of list for playing.



def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count=0;
    for i in range(3):                   #iterating and checking for the filled positions.
        for j in range(3):
            if(board[i][j]!=EMPTY):
                count=count+1;
    if count%2==0:                      #if count is even then 'X' is returned , if it is odd 'O' is returned.
        return X;
    else:
        return O;
       


def actions(board):
    l= []
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:   #appending  all the possible actions which are not filled.
                l.append((i, j))
    return l


def result(board, action):
    i, j = action
    k=[[EMPTY, EMPTY, EMPTY],         # creating a new list , assigning it to board(old list) and updating it.
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    for p in range(3):
        for q in range(3):
            k[p][q]=board[p][q];
    k[i][j] = player(board)
    return k


def winner(board):
    #checking for all posibilities (row-wise,column-wise,diagonal-wise)
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != EMPTY:
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] !=EMPTY:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] !=EMPTY:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None;


def terminal(board):
    count=0;
    for i in range(3):
        for j in range(3):
            if(board[i][j]!=EMPTY):  # counting all the non empty positions
                count=count+1;
    if(count==9 or winner(board)!=None): # if all the positions are filled and winner is none then the game is terminated.
        return True;
    else:
        return False;
    


def utility(board):
    if(winner(board)==X):                     #if X wins returns 1
        return 1
    elif (winner(board)==O):                  #if O wins returns -1
        return -1
    else:
        return 0                              #neither X nor O returns 0


def minimax(board):                     
    def maximum(board):         # returns the maximum of the minmum values.
        if (terminal(board)==True):         #predicting whether its a win or lose or tie.
            return utility(board)
        bestScore= -100;                    
        for i in actions(board):
             if( bestScore < minimum(result(board, i))):     #assigning minimum value to the bestscore.
                bestScore = minimum(result(board, i))
        return bestScore;

    def minimum(board):          #returns the minimum of the maximum values.
        if (terminal(board)==True):             #predicting whether its a win or lose or tie.
            return utility(board)
        bestScore= 100
        for i in actions(board):
            if (bestScore > maximum(result(board, i))):  #assigning maximum value to the bestscore.
               bestScore = maximum(result(board, i))

        return  bestScore;

    if player(board) == X:       
        pos_actions = actions(board)
        bestAction = None
        bestMin = -100

        for i in pos_actions:            
            R = result(board, i)
            mini= minimum(R)
            if mini > bestMin:          #choosing the best action from all possible actions.
                bestMin= mini
                bestAction = i
                
        return bestAction;
    else:
        pos_actions = actions(board)
        bestAction  = None
        bestMax= 100

        for i in pos_actions:
            R= result(board, i)
            maxi = maximum(R)
            if maxi < bestMax:               #choosing the best action from all possible actions.
                bestMax = maxi
                bestAction= i
                
        return bestAction
