# Simple pygame program

# Import and initialize the pygame library
import time

import numpy as np
import pygame

def update_board(board):
    updated_board = np.zeros(board.shape)
    row_dim = board.shape[0]
    col_dim = board.shape[1]
    for i in range(0, row_dim):
        for j in range(0, col_dim):
            if neighborhood_density(board, i, j) < 2:
                updated_board[i][j] = False
            elif neighborhood_density(board, i, j) > 4:
                updated_board[i][j] = False
            else:
                updated_board[i][j] = True
    return updated_board

def neighborhood_density(board, row, col):
    density = 0
    for i in [row-1, row, row+1]:
        for j in [col-1, col, col+1]:
            if i == row and j == col:
                continue
            if i < 0 or j < 0 or i >= board.shape[0] or j >= board.shape[1]:
                continue
            if board[i][j]:
                density += 1
    return density

from pygame.rect import Rect
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit

running = True
lifex = 5
lifey = 6

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    board_dim = 50

    board_values = np.zeros((board_dim, board_dim), dtype=bool)
    board_values[lifex][lifex] = True
    board_values[lifex][lifey] = True
    board_values[lifey][lifex] = True
    print(board_values)
    screen.fill((0, 0, 0))
    i = 0
    j = 0
    sq_size = 10
    while i < board_dim:
        j = 0
        while j < board_dim:
            status = not board_values[i][j]
            pygame.draw.rect(screen, (225*status, 225*status, 225*status), (i*sq_size, j*sq_size, sq_size, sq_size))
            j += 1
        i += 1
    pygame.display.flip()
    time.sleep(1)
    board_values[lifex][lifex] = False
    board_values[lifex][lifey] = False
    board_values[lifey][lifex] = False

    lifex = (lifex+1)%board_dim
    lifey = (lifey+1)%board_dim
    # Flip the display

# Done! Time to quit.
pygame.quit()

