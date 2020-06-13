import pygame


class Boost(pygame.sprite.Sprite):
    def __init__(self, file_image, name, side, rect_x, rect_y):
        super().__init__()
        self.side = side
        self.image = file_image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.x = rect_x + 16
        self.rect.y = rect_y + 16

    def draw(self, surface):
        surface.blit(self.image, self.rect)
