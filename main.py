import numpy as np
import pygame
import math
import sys

Row_Count = 6
Column_Count = 7
Even = 0
Odd = 1


def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[5][col] == 0


def get_next_open_row():
    for r in range(Row_Count):
        if board[r][col] == 0:
            return r


board = create_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = int(input('Player 1 make your move (0-6)'))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

    else:
        col = int(input("Player 2 make your move (0-6)"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    turn += 1
    turn = turn % 2
