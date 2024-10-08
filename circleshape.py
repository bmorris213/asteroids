import pygame

# base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # init based on containers
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        # abstract
        pass
    
    def update(self, dt):
        # abstract
        pass
    
    def collidesWith(self, other):
        distance = pygame.math.Vector2.distance_to(other.position, self.position)
        minDistance = self.radius + other.radius
        return distance <= minDistance