
# Draws a moving block to the window which bounces when it hits edges
# Also draws random 'food' blocks to the window which when hit by the
# main block disappear.


import pygame, sys, random
from pygame.locals import *

def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window
WINDOWHEIGHT = 600
WINDOWWIDTH = 800
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# Set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
MOVESPEED = 8

# Set up colors
BLACK = (0, 0, 0)
GREEN = (3, 178, 20)
PURPLE = (150, 50, 150)

# Set up bouncer and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
bouncer = {'rect':pygame.Rect(300, 100, 50, 50), 'dir':UPLEFT}
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Main game loop
while True:
    # Check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Add more food!
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # Draw black background onto window windowSurface
    windowSurface.fill(BLACK)

    # Move bouncer data structures
    if bouncer['dir'] == DOWNLEFT:
        bouncer['rect'].left -= MOVESPEED
        bouncer['rect'].top += MOVESPEED
    if bouncer['dir'] == DOWNRIGHT:
        bouncer['rect'].left += MOVESPEED
        bouncer['rect'].top += MOVESPEED
    if bouncer['dir'] == UPLEFT:
        bouncer['rect'].left -= MOVESPEED
        bouncer['rect'].top -= MOVESPEED
    if bouncer['dir'] == UPRIGHT:
        bouncer['rect'].left += MOVESPEED
        bouncer['rect'].top -= MOVESPEED

    # Check if bouncer has moved out of the window
    if bouncer['rect'].top < 0:
        # Bouncer has moved past the top
        if bouncer['dir'] == UPLEFT:
            bouncer['dir'] = DOWNLEFT
        if bouncer['dir'] == UPRIGHT:
            bouncer['dir'] = DOWNRIGHT
    if bouncer['rect'].bottom > WINDOWHEIGHT:
        # Bouncer has moved past the bottom
        if bouncer['dir'] == DOWNLEFT:
            bouncer['dir'] = UPLEFT
        if bouncer['dir'] == DOWNRIGHT:
            bouncer['dir'] = UPRIGHT
    if bouncer['rect'].left < 0:
        # Bouncer has moved past left side
        if bouncer['dir'] == DOWNLEFT:
            bouncer['dir'] = DOWNRIGHT
        if bouncer['dir'] == UPLEFT:
            bouncer['dir'] = UPRIGHT
    if bouncer['rect'].right > WINDOWWIDTH:
        # Bouncer has moved past right side
        if bouncer['dir'] == DOWNRIGHT:
            bouncer['dir'] = DOWNLEFT
        if bouncer['dir'] == UPRIGHT:
            bouncer['dir'] = UPLEFT

    # Draw the bouncer onto window surface
    pygame.draw.rect(windowSurface, PURPLE, bouncer['rect'])

     # Check if bouncer as collided with food
    for food in foods[:]:
        if doRectsOverlap(bouncer['rect'], food):
            foods.remove(food)

    # Draw food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # Draw window to screen
    pygame.display.update()
    mainClock.tick(40)
