import pygame
import game_config as gm
from random import randint


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, name, angle):
        super().__init__()
        if name == 'center':
            self.image = gm.FIRE_ITEM[0]
        elif name == 'line':
            self.image = self._rotate_image(gm.FIRE_ITEM[1], angle)
        elif name == 'corner':
            self.image = self._rotate_image(gm.FIRE_ITEM[2], angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.explosion_event = None

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def _rotate_image(self, image, angle):
        return pygame.transform.rotate(image, angle)
