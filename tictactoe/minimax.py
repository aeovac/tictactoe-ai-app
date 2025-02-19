from utilities import win, is_full

def get_best_move(board) -> tuple[int, int]:
    best_score = -10
    move = (-1, -1)
    for i in range(9):
        row, col = divmod(i, 3)
        if board[row][col] == ' ':
            board[row][col] = 'o'
            score = minimax(board, 0, False)
            board[row][col] = ' '
            if score > best_score:
                best_score = score
                move = (row, col)              
    board[move[0]][move[1]] = 'o'
    return move

def minimax(
    board,
    depth, 
    maximizing_player
):
    if win(board, 'x'):
        return -1
    elif win(board, 'o'):
        return 1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = -10
        for i in range(9):
            row, col = divmod(i, 3)
            if board[row][col] == ' ':
                board[row][col] = 'o'
                eval = minimax(board, depth + 1, False)
                board[row][col] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = 10
        for i in range(9):
            row, col = divmod(i, 3)
            if board[row][col] == ' ':
                board[row][col] = 'x'
                eval = minimax(board, depth + 1, True)
                board[row][col] = ' '
                min_eval = min(min_eval, eval)
        return min_eval