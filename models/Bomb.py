import pygame
import time

class Bomb(pygame.sprite.Sprite):
    def __init__(self,image,rect_center_x, rect_center_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [rect_center_x, rect_center_y]
        self.time_life = 2

    def update(self):

