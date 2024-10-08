import pygame
from constants import *

def main():
    # initialize game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.Surface.fill(screen, (0,0,0))

    # create game time
    timer = pygame.time.Clock()
    dt = 0

    # start of game loop
    while True:
        # frame limit, delta time, in seconds
        dt = timer.tick(FRAMES_PER_SECOND) / 1000

        # check for window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # redraw screen
        pygame.display.flip()

if __name__ == "__main__":
    main()