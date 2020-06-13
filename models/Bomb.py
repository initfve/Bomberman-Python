import pygame
from random import randint


class Bomb(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.fire_event = pygame.USEREVENT + randint(1, 7)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.explosion_event = pygame.USEREVENT + randint(1, 5)

    def update(self):
        pass

