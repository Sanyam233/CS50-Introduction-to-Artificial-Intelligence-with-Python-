"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # return [["X", "X", "O"],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, "O"]]

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turn_count = [0,0,0] # [X, 0, E]

    #counts the number of X,O and Empty positions on the board and stores it in turn_count
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                turn_count[0] +=1
            elif board[i][j] == O:
                turn_count[1] +=1
            else:
                turn_count[2] +=1

    if turn_count[2] == 9 or (turn_count[1] >= turn_count[0]):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    poss_actions = []
    push = poss_actions.append
    #counts the number of X,O and Empty positions on the board and stores it in turn_count
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                push((i, j)) #(row index, col index)

    return poss_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_turn = player(board)

    board_cpy = deepcopy(board)

    if board_cpy[action[0]][action[1]] == EMPTY:
        board_cpy[action[0]][action[1]] = player_turn
        return board_cpy
    else:
        raise ValueError #change it with a own created error


def decider(array):
    resp = array.count(array[0]) == len(array)
    if (resp == True):
        if(array[0] == X):
            return X
        elif (array[0] == O):
            return O    
    return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    res = None
    #horizontal check
    for i in range(3):
        row = board[i]
        res = decider(row)
        if(res != None):
            return res
    
    #vertical check 
    checker = []
    for j in range(3):
        for i in range(3):
            checker.append(board[i][j])
        res = decider(checker)
        if(res != None):
            return res
        checker = []
    
    #diagonal check
    if((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])):
        if(board[1][1] == X):
            return X
        elif (board[1][1] == O):
            return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    res = winner(board)

    if res != None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 10 if X has won the game, -10 if O has won, 0 otherwise.
    """
    res = winner(board)

    if res == X:
        return 1
    elif res == O:
        return -1
    else:
        return 0


def board_utility(board,beta, alpha, maximizer):


    if(terminal(board)):
        return utility(board)
    else:

        if(maximizer):
            maximum = -math.inf
            for pair in actions(board):
                updated_board = result(board, pair)
                score = board_utility(updated_board,beta, alpha, False)
                maximum = max(maximum, score)
                alpha = max(score, alpha)
                if(beta <= alpha):
                    break
            return maximum
        else:
            minimum = math.inf
            for pair in actions(board):
                updated_board = result(board, pair)
                score = board_utility(updated_board,beta, alpha, True)       
                minimum = min(minimum, score)
                beta = min(score, beta)
                if(beta <= alpha):
                    break
            return minimum




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_score = -1000
    best_move = tuple()
    maximizer = True
    x_or_o = player(board)

    if(x_or_o == X):
        best_score = -math.inf
    else:
        best_score = math.inf

    for pair in actions(board):  
        updated_board = result(board, pair)
        if(player(updated_board) == X):
            maximizer = True
        else:
            maximizer = False
        score = board_utility(updated_board,math.inf, -math.inf, maximizer)

        if(x_or_o == X and score >= best_score):
            best_score = score
            best_move = pair
        elif (x_or_o == O and score <= best_score):
            best_score = score
            best_move = pair
    return best_move

# minimax(initial_state())


