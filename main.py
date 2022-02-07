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


def drop_piece():
    pass


def is_valid_location():
    pass


def get_next_open_row():
    pass


board = create_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = int(input('Player 1 make your move (0-6)'))

    else:
        col = int(input("Player 2 make your move (0-6)"))

    turn += 1
    turn = turn % 2
