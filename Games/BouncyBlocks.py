
# Do you like bouncy things? Me too. Here are some bouncing blocks.

import pygame, sys, time
from pygame.locals import *

pygame.init()

# Window
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Python Animation - Bounce! BOUNCE!!')

# Direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
MOVESPEED = 3

# Colors
BLACK = (0, 0, 0)
RED = (255, 153, 18)
GREEN = (3, 178, 20)
BLUE = (70, 0, 255)
PURPLE = (150, 50, 150)

# Block data structure
b1 = {'rect':pygame.Rect(300, 80, 30, 30), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 30, 30), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 30, 30), 'color':BLUE, 'dir':DOWNLEFT}
b4 = {'rect':pygame.Rect(400, 50, 30, 30), 'color':PURPLE, 'dir':DOWNLEFT}
blocks = [b1, b2, b3, b4]

# Game loop
while True:
    # Check for QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Draw black background onto surface
    windowSurface.fill(BLACK)
    for b in blocks:
        #Move the block data structure
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        # Check if block is out of the window
        if b['rect'].top < 0:
            # Block has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            # Block has moved past bottom
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # Block has moved past left side
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            # Block has moved past right side
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

        # Draw blocks onto the surface
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    # Draw window onto screen
    pygame.display.update()
    time.sleep(0.02)

