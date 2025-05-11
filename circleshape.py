import pygame
#Base clss for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        #we will using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    def draw(self, screen):
        #sub-classes must override
        pass
    def update(self, dt):
        #sub-classes must override
        pass
    def collides_with(self, other):
        #check if two circles are colliding
        min_distance = self.radius + other.radius
        actuell_distance=self.position.distance_to(other.position)
        # if(actuell_distance <= min_distance):
        #     print(actuell_distance, min_distance)
        # return actuell_distance <= min_distance
        return self.position.distance_to(other.position) <= self.radius + other.radius
     