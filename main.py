# Simple pygame program

# Import and initialize the pygame library
import time

import numpy as np
import pygame
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