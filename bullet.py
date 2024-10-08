from circleshape import CircleShape
import pygame
from constants import BULLET_RADIUS

class Bullet(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)