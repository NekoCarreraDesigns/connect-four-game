import numpy as np
import pygame
import math
import sys

Blue = (0, 11, 235)
Black = (1, 2, 3)
Red = (240, 0, 0)
Yellow = (255, 255, 0)

Row_Count = 6
Column_Count = 7


def create_board():
    board = np.zeros((Row_Count, Column_Count))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[Row_Count-1][col] == 0


def get_next_open_row(board, col):
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
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def draw_board(board):
    for c in range(Column_Count):
        for r in range(Row_Count):
            pygame.draw.rect(screen, Blue, (c*SquareSize, r *
                             SquareSize+SquareSize, SquareSize, SquareSize))
            pygame.draw.circle(screen, Black, (int(
                c*SquareSize+SquareSize/2), int(r*SquareSize+SquareSize+SquareSize/2)), radius)

    for c in range(Column_Count):
        for r in range(Row_Count):
            if board[r][c] == 1:
                pygame.draw.circle(screen, Red, (int(
                    c*SquareSize+SquareSize/2), height-int(r*SquareSize+SquareSize/2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, Yellow, (int(
                    c*SquareSize+SquareSize/2), height-int(r*SquareSize+SquareSize/2)), radius)

    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SquareSize = 100

width = Column_Count * SquareSize
height = (Row_Count+1) * SquareSize

size = (width, height)
radius = int(SquareSize/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, Black, (0, 0, width, SquareSize))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(
                    screen, Red, (posx, int(SquareSize/2)), radius)
            else:
                pygame.draw.circle(
                    screen, Yellow, (posx, int(SquareSize/2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, Black, (0, 0, width, SquareSize))
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SquareSize))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render(
                            "Player 1 wins!!, Yaaaayy!!", 1, Red)
                        screen.blit(label, (40, 10))
                        game_over = True

            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SquareSize))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render(
                            "Player 2 wins!!, Yaaaayy!!", 2, Yellow)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
