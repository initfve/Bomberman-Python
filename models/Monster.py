import pygame
import game_config as gm


# Klasa przeciwnika
class Monster(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.movement_x = 0
        self.movement_y = 0
        self._count = 0
        self.lifes = 3
