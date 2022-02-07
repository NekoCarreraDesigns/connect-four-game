import numpy as np
import pygame
import math
import sys

Row_Count = 6
Column_Count = 7
Even = 0
Odd = 1


def create_board():
    board = np.zeros((Row_Count, Column_Count))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[Row_Count-1][col] == 0


def get_next_open_row():
    for r in range(Row_Count):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    for c in range(Column_Count - 3):
        for r in range(Row_Count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    for c in range(Column_Count):
        for r in range(Row_Count - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    for c in range(Column_Count - 3):
        for r in range(Row_Count - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    for c in range(Column_Count):
        for r in range(3, Row_Count):
            if board[r][c] == piece and board[r-1][c] == piece and board[r-2][c] == piece and board[r-3][c] == piece:
                return True


board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = int(input('Player 1 make your move (0-6)'))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("Player 1 wins!!! Yaaaaay!!!")
                game_over = True

    else:
        col = int(input("Player 2 make your move (0-6)"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("Player 2 wins!!! Yaaaaay!!!")
                game_over = True
                break

    print_board(board)

    turn += 1
    turn = turn % 2
