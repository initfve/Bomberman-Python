import pygame
from random import randint


class Explosion:
    def __init__(self, x, y):
        super().__init__()
        self.image =
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.explosion_event = pygame.USEREVENT + randint(1, 5)

    def update(self):
        pass