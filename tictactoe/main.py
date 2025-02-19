import tkinter as tk
from tkinter import messagebox
from time import sleep

from utilities import win, is_full, transform
from minimax import get_best_move

def run():
    root = tk.Tk()
    root.title('TicTacToe')
    root.geometry('240x245')
    
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    for i in range(9):
        row, col = divmod(i, 3)
        button = tk.Button(
            root,
            text=' ',
            bg='white',
            fg='black',
            width=10,
            height=5,
            command=lambda r=row, c=col: on_interaction(board, r, c)
        )
        button.grid(row=row, column=col)
        board[row][col] = button

    def on_interaction(board, row, column):
        _board = transform(board)
        
        if _board[row][column] != ' ':
            messagebox.showinfo('This cell is already use')
            return
        
        _board[row][column] = 'x'   
        board[row][column]['text'] = 'x'
        
        if win(_board, 'x'):
            messagebox.showinfo(message='Player win!')
        elif is_full(_board):
            messagebox.showinfo(message='Draw!')
        else:
            move = get_best_move(_board)
            sleep(0.8)
            _board[move[0]][move[1]] = 'o'
            board[move[0]][move[1]]['text'] = 'o'

            if win(_board, 'o'):
                messagebox.showinfo(message='AI win')

        print(row, column, 'x')
    root.mainloop()
    pass

run()