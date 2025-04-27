import pygame

class Player:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        self.speed = 200
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)

        #direction
        self.up, self.down, self.right, self.left = 0, 0, 0, 0

    def update(self, dt):
        self.rect.x += (self.right - self.left) * self.speed * dt
        self.rect.y += (self.down - self.up) * self.speed * dt

    def get_pos(self):
        return [self.rect.x, self.rect.y]