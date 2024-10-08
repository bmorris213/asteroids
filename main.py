import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    # initialize game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create game time
    timer = pygame.time.Clock()
    dt = 0

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # assign groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (bullets, updatable, drawable)

    # create objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    # start of game loop
    while True:
        # frame limit, delta time, in seconds
        dt = timer.tick(FRAMES_PER_SECOND) / 1000

        # check for window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # blank out screen
        pygame.Surface.fill(screen, (0,0,0))

        # update groups
        for item in updatable:
            item.update(dt)

        # detect asteroid collisions
        for item in asteroids:
            # player collisions
            if item.collidesWith(player):
                print("GAME OVER! lool")
                sys.exit(0)

            # bullet collisions
            for shot in bullets:
                if item.collidesWith(shot):
                    shot.kill()
                    item.split()

        # draw groups
        for item in drawable:
            item.draw(screen)
        
        # redraw screen
        pygame.display.flip()

if __name__ == "__main__":
    main()