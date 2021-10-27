
import time

import numpy as np
import pygame

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
board_values = np.zeros((board_dim, board_dim), dtype=bool)
for i in range(0, board_dim):
    for j in range(0, board_dim):
        board_values[i][j] = i%2 == j%2

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

        draw_board(board_values, sq_size)

pygame.quit()
