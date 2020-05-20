from random import randint

import pygame
import game_config as gm


# Klasa przeciwnika
class Monster(pygame.sprite.Sprite):
    def __init__(self, file_image, life_count, side, rect_x, rect_y):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.movementX = 0
        self.movementY = 0
        self._count = 0
        self._lifeCount = life_count
        self.level = None
        self.direction = randint(0, 3)
        self.directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.side = side
        self.rect.x = rect_x
        self.rect.y = rect_y

    def update(self, *args):
        # self._move(self.directions[self.direction], 9)
        self.rect.x += self.movementX
        self.rect.y += self.movementY

        colliding_obstacles = pygame.sprite.spritecollide(self, self.level.set_of_obstacles, False)
        colliding_squares = pygame.sprite.spritecollide(self, self.level.set_of_squares, False)
        ##collids.append(colliding_squares)

        for p in colliding_obstacles.union(colliding_squares):
            if self.movementX > 0:
                self.rect.right = p.rect.left
            if self.movementX < 0:
                self.rect.left = p.rect.right
            if self.movementY > 0:
                self.rect.bottom = p.rect.top
            if self.movementY < 0:
                self.rect.top = p.rect.bottom

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def stop(self):
        self.movementX = 0
        self.movementY = 0

    # direction should be f. e. { x: 1, y: 1} is right, down, { x: -1, y: -1} is left, up
    def _move(self, direction, speed):
        dx, dy = direction
        self.movementX = dx * speed
        self.movementY = dy * speed

    def _die(self):
        pass
