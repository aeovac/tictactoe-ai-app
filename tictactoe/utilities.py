
def transform(board):
    return [[board[i][j]['text'] for j in range(3)] for i in range(3)]

def win(board, player):
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
def is_full(board):
    for _ in board:
        if ' ' in _:
            return False
    return True