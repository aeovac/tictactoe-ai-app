import random

def ai_move(board):
    move = get_best_move(board)
    board[move[0]][move[1]] = 'o'

def player_move(board):
    while True:
        row = int(input('Enter row (1-3): ')) - 1
        col = int(input('Enter column (1-3): ')) - 1
        if board[row][col] == ' ':
            board[row][col] = 'x'
            break
        else:
            print('Cell already occupied. Try again.')

def draw_board(board):
    for x, row in enumerate(board):
        print(' | '.join(row))
        if x != 2: print('___' * 3 )
    print()
    
def get_best_move(board):
    best_score = -10
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'o'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = 'o'
    return move    

def check_win(board, player):
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
def minimax(board, depth, maximizing_player):
    if check_win(board, 'x'):
        return -1
    elif check_win(board, 'o'):
        return 1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = -10
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'o'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = 10
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'x'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval
    
    
def is_ai_trun(player):
    return player == 1

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    player = random.randint(0, 1)
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    while True:
        draw_board(board)
        player_move(board)
        if check_win(board, 'x'):
            draw_board(board)
            print('Player wins!')
            break
        elif is_full(board):
            draw_board(board)
            print('It\'s a draw!')
            break
        ai_move(board)
        if check_win(board, 'o'):
            draw_board(board)
            print('AI wins!')
            break
        

if __name__ == '__main__':
    main()