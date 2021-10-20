# Simple pygame program

# Import and initialize the pygame library
import time

import numpy as np
import pygame

def update_board(board):
    updated_board = np.zeros(board.shape)
    for i in range(0, board.shape[0]):
        for j in range(0, board.shape[1]):
            if board[i, j]:
                if neighborhood_density(board, i, j) < 2:
                    updated_board[i][j] = False
                elif neighborhood_density(board, i, j) > 3:
                    updated_board[i][j] = False
                else:
                    updated_board[i][j] = True
            else:
                if neighborhood_density(board, i, j) == 3:
                    updated_board[i][j] = True
    return updated_board

def neighborhood_density(board, row, col):
    density = 0
    for i in [row-1, row, row+1]:
        for j in [col-1, col, col+1]:
            if i == row and j == col:
                None
            elif i < 0 or i >= board.shape[0] or j < 0 or j >= board.shape[1]:
                None
            else:
                density += board[i][j]
    return density

def draw_board(board, sq_size):
    for i in range(0, board.shape[0]):
        for j in range(0, board.shape[1]):
            color = [225, 225, 225]
            print(color)
            status = not board_values[i][j]
            print(type(color))
            color = [x * status for x in color]
            print(type(color))
            print(color)
            pygame.draw.rect(screen, color, (i*sq_size, j*sq_size, sq_size, sq_size))
            j += 1
        i += 1
    pygame.display.flip()

from pygame.rect import Rect
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit

running = True
mat = [[0, 1, 1, 1, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

board_dim = 50

board_values = np.zeros((board_dim, board_dim), dtype=bool)
for i in range(0, 5):
    for j in range(0, 5):
        board_values[i+30][j+30] = mat[i][j]
screen.fill((0, 0, 0))
sq_size = 10

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board(board_values, sq_size)
    board_values = update_board(board_values)
    time.sleep(1)

    # Flip the display

# Done! Time to quit.
pygame.quit()

