from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def split(self):
        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        randomAngle = random.uniform(20, 50)
        vectorA = pygame.math.Vector2.rotate(self.velocity, randomAngle)
        vectorB = pygame.math.Vector2.rotate(self.velocity, -randomAngle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        asteroidA = Asteroid(self.position.x, self.position.y, newRadius)
        asteroidA.velocity = vectorA * 1.2
        asteroidB = Asteroid(self.position.x, self.position.y, newRadius)
        asteroidB.velocity = vectorB * 1.2