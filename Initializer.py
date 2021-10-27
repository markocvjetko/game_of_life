"""
Used for generating initial game of life board state. The user selects squares
"""
import time

import numpy as np
import pandas as pd
import pygame
from numpy import matrix

from pygame.rect import Rect

def draw_board(board, sq_size):
    for i in range(0, board.shape[0]):
        for j in range(0, board.shape[1]):
            color = [225, 225, 225]
            status = not board_values[i][j]
            color = [x * status for x in color]
            pygame.draw.rect(screen, color, (i*sq_size, j*sq_size, sq_size, sq_size))
            j += 1
        i += 1
    pygame.display.flip()

pygame.init()

screen = pygame.display.set_mode([500, 500])

screen.fill((0, 0, 0))
sq_size = 100
board_dim = 5
board_values = np.genfromtxt('initial_state.csv', delimiter=",", dtype=bool)
print(board_values)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            x = pos[0] // sq_size
            y = pos[1] // sq_size
            board_values[x][y] = int((board_values[x][y]+1)%2)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                df = pd.DataFrame(board_values)
                df.to_csv("initial_state.csv", index=False, header=False)
                print("Board state saved")

    draw_board(board_values, sq_size)
pygame.quit()
